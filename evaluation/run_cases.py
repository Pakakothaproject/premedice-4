#!/usr/bin/env python3
"""Collect Premedice answers for an evaluation case file.

This only collects outputs. It does not score them and it makes no clinical
claim. Use score_clinical.py with clinician adjudication afterward.
"""

import argparse
import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

DEFAULT_BASE = "https://api.premedice.com"
DEFAULT_MODEL = "Premedice/Premed-4"


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise SystemExit(f"{path}:{number}: invalid JSON: {exc}") from exc
    return rows


def answer_body(body: dict[str, Any]) -> str:
    try:
        return body["choices"][0]["message"]["content"] or ""
    except (KeyError, IndexError, TypeError):
        return ""


def source_list(body: dict[str, Any]) -> list[Any]:
    meta = body.get("premedice_meta")
    if isinstance(meta, dict) and isinstance(meta.get("sources"), list):
        return meta["sources"]
    citations = body.get("citations")
    return citations if isinstance(citations, list) else []


def run_case(base: str, model: str, key: str, case: dict[str, Any], timeout: float) -> dict[str, Any]:
    payload = {
        "model": model,
        "temperature": 0,
        "stream": False,
        "messages": [{"role": "user", "content": case["prompt"]}],
    }
    request = urllib.request.Request(
        f"{base.rstrip('/')}/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "premedice-evaluation/1.0",
        },
        method="POST",
    )
    started = time.perf_counter()
    status = 0
    body: dict[str, Any] = {}
    error = None
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            status = response.status
            parsed = json.loads(response.read().decode("utf-8", errors="replace"))
            body = parsed if isinstance(parsed, dict) else {}
    except urllib.error.HTTPError as exc:
        status = exc.code
        error = f"http_{exc.code}"
    except Exception as exc:  # noqa: BLE001
        error = type(exc).__name__

    return {
        "id": case["id"],
        "category": case.get("category"),
        "status": status,
        "error": error,
        "latency_ms": round((time.perf_counter() - started) * 1000),
        "answer": answer_body(body),
        "sources": source_list(body),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--base-url", default=os.getenv("PREMEDICE_BASE_URL", DEFAULT_BASE))
    parser.add_argument("--model", default=os.getenv("PREMEDICE_MODEL", DEFAULT_MODEL))
    parser.add_argument("--timeout", type=float, default=120.0)
    args = parser.parse_args()

    key = os.getenv("PREMEDICE_API_KEY")
    if not key:
        raise SystemExit("PREMEDICE_API_KEY is required")

    cases = load_jsonl(args.cases)
    rows = [run_case(args.base_url, args.model, key, case, args.timeout) for case in cases]
    args.out.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")
    print(f"Wrote {len(rows)} answers to {args.out}")
    return 0 if all(row["status"] == 200 for row in rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
