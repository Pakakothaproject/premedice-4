# Premedice 4 — Evaluation Harness

**Status:** Protocol tooling. No clinical results are published here.  
**Target:** 100 clinician-adjudicated cases.

---

## What this is

A reproducible harness for the 100-case clinical evaluation:

1. `cases.jsonl` — de-identified clinical cases with expected red flags and source types.
2. `run_cases.py` — calls the Premedice API and saves answers, sources, and latency.
3. `score_clinical.py` — joins clinician adjudication and computes the headline metrics.
4. `REPORT_TEMPLATE.md` — the report format for publication.

## What this is not

This is not a benchmark result. The example cases and adjudication are synthetic, included only to show the format. Do not publish a score computed from them.

## Files

- `cases.schema.json` — case format.
- `cases.example.jsonl` — 8 synthetic examples, not real patients.
- `adjudication.template.csv` — reviewer form.
- `adjudication.example.csv` — sample values for tool testing only.
- `run_cases.py` — API collection runner.
- `score_clinical.py` — clinical scoring.
- `REPORT_TEMPLATE.md` — results report.

## Collect answers

```bash
export PREMEDICE_API_KEY="pm_live_..."
export PREMEDICE_BASE_URL="https://api.premedice.com"
export PREMEDICE_MODEL="Premedice/Premed-4"

python3 run_cases.py \
  --cases cases.example.jsonl \
  --out answers.jsonl
```

## Adjudicate

Two independent clinicians fill one row per case in a copy of
`adjudication.template.csv`:

- `citation_support`: `supported`, `unsupported`, or `not_applicable`
- `red_flag_caught`: `yes`, `no`, or `not_applicable`
- `unsupported_claim`: `yes` or `no`
- `reviewer`: reviewer ID
- `notes`: short reason

Resolve disagreements with a third reviewer and record the final row.

## Score

```bash
python3 score_clinical.py \
  --cases cases.example.jsonl \
  --answers answers.jsonl \
  --adjudication adjudication.csv \
  --out results.json \
  --csv results.csv
```

The scorer refuses to produce a headline result with fewer than 100 cases unless
`--allow-small` is passed. Use `--allow-small` only for harness testing.

Metrics:

- citation precision
- red-flag recall
- unsupported-claim rate
- adjudication coverage
- latency p50/p95
- per-category breakdown

## Publication rules

- Report numerators and denominators.
- Report clinician disagreements.
- Report failures, not only successes.
- Do not compare against another product unless it was evaluated on the same cases.
- MedQA or any exam score is not a substitute for this evaluation.
