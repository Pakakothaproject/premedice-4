#!/usr/bin/env python3
"""Structural smoke-test runner for the Premedice 4 API.

This is not clinical validation. It checks response shape, sources, emergency
language, uncertainty language, disclaimers, and latency on synthetic cases.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_BASE_URL = "https://api.premedice.com"
DEFAULT_MODEL = "Premedice/Premed-4"

EMERGENCY = re.compile(
    r"(911|999|112|emergency services|emergency department|call emergency|"
    r"seek urgent|go to the er|go to a&e|immediate medical|"
    r"988|crisis lifeline|suicide.*crisis)",
    re.IGNORECASE,
)
DISCLAIMER = re.compile(
    r"(not medical advice|not a diagnosis|not a substitute|"
    r"talk to (your|a) (doctor|clinician)|licensed clinician|"
    r"decision support|information tool)",
    re.IGNORECASE,
)
UNCERTAINTY = re.compile(
    r"(not established|insufficient|uncertain|unclear|cannot determine|"
    r"can't determine|need more information|missing|not enough evidence)",
    re.IGNORECASE,
)


def load_cases(path: Path) -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            line = line.strip()
            if not line:
                continue
            try:
                case = json.loads(line)
            except json.JSONDecodeError as exc:
                raise SystemExit(f"{path}:{line_number}: invalid JSON: {exc}") from exc
            if not case.get("id") or not case.get("prompt"):
                raise SystemExit(f"{path}:{line_number}: id and prompt are required")
            cases.append(case)
    return cases


def source_count(body: dict[str, Any]) -> int:
    meta = body.get("premedice_meta")
    if isinstance(meta, dict):
        sources = meta.get("sources")
        if isinstance(sources, list):
            return len(sources)
    citations = body.get("citations")
    if isinstance(citations, list):
        return len(citations)
    return 0


def answer_text(body: dict[str, Any]) -> str:
    choices = body.get("choices")
    if isinstance(choices, list) and choices:
        message = choices[0].get("message") if isinstance(choices[0], dict) else None
        if isinstance(message, dict):
            content = message.get("content")
            if isinstance(content, str):
                return content
    return ""


def run_case(
    base_url: str,
    model: str,
    api_key: str,
    case: dict[str, Any],
    timeout: float,
) -> dict[str, Any]:
    payload = {
        "model": model,
        "temperature": 0,
        "stream": False,
        "messages": [{"role": "user", "content": case["prompt"]}],
    }
    request = urllib.request.Request(
        f"{base_url.rstrip('/')}/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )

    started = time.perf_counter()
    status = 0
    body: dict[str, Any] = {}
    error: str | None = None
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            status = response.status
            raw = response.read().decode("utf-8", errors="replace")
            try:
                parsed = json.loads(raw)
                body = parsed if isinstance(parsed, dict) else {}
            except json.JSONDecodeError:
                error = "invalid_json_response"
    except urllib.error.HTTPError as exc:
        status = exc.code
        error = f"http_{exc.code}"
    except Exception as exc:  # noqa: BLE001 - report whatever the client sees
        error = type(exc).__name__

    elapsed_ms = round((time.perf_counter() - started) * 1000)
    text = answer_text(body)
    expect = case.get("expect") or {}
    metadata_sources = source_count(body)
    inline_sources = len(re.findall(r"https?://", text))
    sources = max(metadata_sources, inline_sources)
    checks = {
        "http_ok": status == 200 and error is None,
        "non_empty": bool(text.strip()),
        "sources_present": sources > 0 if expect.get("sources") else True,
        "emergency_language": bool(EMERGENCY.search(text)) if expect.get("emergency") else True,
        "uncertainty_language": bool(UNCERTAINTY.search(text)) if expect.get("uncertainty") else True,
        "disclaimer_language": bool(DISCLAIMER.search(text)) if expect.get("disclaimer") else True,
    }
    return {
        "id": case["id"],
        "category": case.get("category"),
        "status": status,
        "error": error,
        "latency_ms": elapsed_ms,
        "answer_chars": len(text),
        "sources": sources,
        "metadata_sources": metadata_sources,
        "inline_sources": inline_sources,
        "checks": checks,
        "passed": all(checks.values()),
    }


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = [
        "id",
        "category",
        "status",
        "error",
        "latency_ms",
        "answer_chars",
        "sources",
        "passed",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key) for key in fields})


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--csv", type=Path)
    parser.add_argument("--base-url", default=os.getenv("PREMEDICE_BASE_URL", DEFAULT_BASE_URL))
    parser.add_argument("--model", default=os.getenv("PREMEDICE_MODEL", DEFAULT_MODEL))
    parser.add_argument("--timeout", type=float, default=120.0)
    args = parser.parse_args()

    api_key = os.getenv("PREMEDICE_API_KEY")
    if not api_key:
        print("PREMEDICE_API_KEY is required", file=sys.stderr)
        return 2

    cases = load_cases(args.cases)
    rows = [
        run_case(args.base_url, args.model, api_key, case, args.timeout)
        for case in cases
    ]

    passed = sum(1 for row in rows if row["passed"])
    latencies = sorted(row["latency_ms"] for row in rows if row["status"] == 200)
    summary = {
        "cases": len(rows),
        "passed": passed,
        "failed": len(rows) - passed,
        "http_errors": sum(1 for row in rows if row["status"] != 200),
        "latency_ms": {
            "min": latencies[0] if latencies else None,
            "median": latencies[len(latencies) // 2] if latencies else None,
            "max": latencies[-1] if latencies else None,
        },
    }
    report = {
        "run": {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "base_url": args.base_url,
            "model": args.model,
            "case_file": str(args.cases),
        },
        "summary": summary,
        "cases": rows,
        "important": (
            "Structural checks only. This is not clinical validation and does not "
            "measure citation precision, red-flag recall, or medical correctness."
        ),
    }
    args.out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    if args.csv:
        write_csv(args.csv, rows)

    print(json.dumps(summary, indent=2))
    return 0 if summary["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
