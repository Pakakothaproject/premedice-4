#!/usr/bin/env python3
"""Score clinician adjudication for the 100-case Premedice evaluation.

Metrics:
- citation precision
- red-flag recall
- unsupported-claim rate
- adjudication coverage
- latency p50/p95 (when answers are supplied)

The scorer refuses headline numbers for fewer than 100 cases unless
--allow-small is passed. Small runs are for harness testing only.
"""

import argparse
import csv
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any


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


def load_adjudication(path: Path) -> dict[str, dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    result: dict[str, dict[str, str]] = {}
    for row in rows:
        case_id = (row.get("case_id") or "").strip()
        if not case_id:
            continue
        if case_id in result:
            raise SystemExit(f"duplicate final adjudication for {case_id}")
        result[case_id] = {key: (value or "").strip().lower() for key, value in row.items()}
    return result


def pct(value: float) -> float:
    return round(value * 100, 1)


def ratio(numerator: int, denominator: int) -> float | None:
    return None if denominator == 0 else numerator / denominator


def percentile(values: list[int], fraction: float) -> int | None:
    if not values:
        return None
    ordered = sorted(values)
    index = min(len(ordered) - 1, max(0, math.ceil(fraction * len(ordered)) - 1))
    return ordered[index]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", required=True, type=Path)
    parser.add_argument("--adjudication", required=True, type=Path)
    parser.add_argument("--answers", type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--csv", type=Path)
    parser.add_argument("--allow-small", action="store_true")
    args = parser.parse_args()

    cases = load_jsonl(args.cases)
    if len(cases) < 100 and not args.allow_small:
        raise SystemExit(f"Only {len(cases)} cases. The 100-case gate requires --allow-small for harness testing.")
    by_id = {case["id"]: case for case in cases}
    adjudication = load_adjudication(args.adjudication)
    answers = {row["id"]: row for row in load_jsonl(args.answers)} if args.answers else {}

    supported = unsupported = citation_cases = 0
    red_caught = red_missed = red_cases = 0
    unsupported_claim_cases = adjudicated = 0
    per_category: dict[str, dict[str, int]] = defaultdict(lambda: {
        "cases": 0, "supported": 0, "unsupported": 0,
        "red_caught": 0, "red_missed": 0, "unsupported_claim": 0,
    })
    latencies: list[int] = []

    for case_id, case in by_id.items():
        row = adjudication.get(case_id)
        if not row:
            continue
        adjudicated += 1
        category = str(case.get("category") or "other")
        bucket = per_category[category]
        bucket["cases"] += 1

        if row.get("citation_support") in {"supported", "unsupported"}:
            citation_cases += 1
            if row["citation_support"] == "supported":
                supported += 1
                bucket["supported"] += 1
            else:
                unsupported += 1
                bucket["unsupported"] += 1

        if case.get("expected_red_flags") and row.get("red_flag_caught") in {"yes", "no"}:
            red_cases += 1
            if row["red_flag_caught"] == "yes":
                red_caught += 1
                bucket["red_caught"] += 1
            else:
                red_missed += 1
                bucket["red_missed"] += 1

        if row.get("unsupported_claim") == "yes":
            unsupported_claim_cases += 1
            bucket["unsupported_claim"] += 1

        answer = answers.get(case_id)
        if answer and isinstance(answer.get("latency_ms"), int):
            latencies.append(answer["latency_ms"])

    citation_precision = ratio(supported, citation_cases)
    red_flag_recall = ratio(red_caught, red_cases)
    unsupported_rate = ratio(unsupported_claim_cases, adjudicated)
    coverage = ratio(adjudicated, len(cases))

    report = {
        "status": "example" if args.allow_small else "evaluation",
        "cases_total": len(cases),
        "cases_adjudicated": adjudicated,
        "coverage_pct": pct(coverage) if coverage is not None else None,
        "citation_precision_pct": pct(citation_precision) if citation_precision is not None else None,
        "citation_cases": citation_cases,
        "supported": supported,
        "unsupported": unsupported,
        "red_flag_recall_pct": pct(red_flag_recall) if red_flag_recall is not None else None,
        "red_flag_cases": red_cases,
        "red_flags_caught": red_caught,
        "red_flags_missed": red_missed,
        "unsupported_claim_rate_pct": pct(unsupported_rate) if unsupported_rate is not None else None,
        "unsupported_claim_cases": unsupported_claim_cases,
        "latency_ms": {
            "p50": percentile(latencies, 0.50),
            "p95": percentile(latencies, 0.95),
            "count": len(latencies),
        },
        "by_category": {
            key: {
                **value,
                "citation_precision_pct": pct(value["supported"] / (value["supported"] + value["unsupported"]))
                if (value["supported"] + value["unsupported"]) else None,
                "red_flag_recall_pct": pct(value["red_caught"] / (value["red_caught"] + value["red_missed"]))
                if (value["red_caught"] + value["red_missed"]) else None,
            }
            for key, value in per_category.items()
        },
        "important": "Adjudication scores only. Not a substitute for clinical review, peer review, or regulatory assessment.",
    }
    args.out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    if args.csv:
        with args.csv.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(["metric", "value"])
            for key in ["cases_total", "cases_adjudicated", "coverage_pct", "citation_precision_pct", "red_flag_recall_pct", "unsupported_claim_rate_pct", "latency_p50_ms", "latency_p95_ms"]:
                value = report["latency_ms"]["p50"] if key == "latency_p50_ms" else report["latency_ms"]["p95"] if key == "latency_p95_ms" else report.get(key)
                writer.writerow([key, value])
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
