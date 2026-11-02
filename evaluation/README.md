# Premedice 4 — Public Evaluation Harness

**Status:** Structural harness, not a clinical validation study
**Last updated:** 3 November 2026

---

## What this is

A small, runnable harness for checking whether the public API returns:

- a non-empty answer
- sources where the case expects them
- emergency language where the case expects escalation
- explicit uncertainty where evidence is missing
- a disclaimer / decision-support boundary

It also records latency and HTTP errors.

## What this is not

This is **not** clinical accuracy validation.

It does not know whether the medical content is correct. It cannot measure citation precision, red-flag recall, or unsupported-claim rate against a clinical reference standard. Those require the clinician-adjudicated protocol in [../docs/evaluation.md](../docs/evaluation.md).

## Files

- `cases.example.jsonl` — 12 synthetic, non-PHI cases.
- `run_eval.py` — stdlib-only runner against an OpenAI-compatible endpoint.
- `REPORT_TEMPLATE.md` — report format for a run.

## Run

```bash
export PREMEDICE_API_KEY="pm_live_..."
export PREMEDICE_BASE_URL="https://api.premedice.com"
export PREMEDICE_MODEL="Premedice/Premed-4"
python3 run_eval.py \
  --cases cases.example.jsonl \
  --out results.json
```

Optional:

```bash
python3 run_eval.py \
  --cases cases.example.jsonl \
  --out results.json \
  --csv results.csv \
  --timeout 120
```

## Output

The JSON report contains:

- `run`: timestamp, base URL, model, case count
- `summary`: structural pass counts and latency
- `cases`: per-case status, latency, answer length, source count, flags

## Interpretation

A structural pass means the response had the expected shape. It does not mean the answer was clinically correct.

Do not publish a clinical accuracy claim from this harness. Use it for smoke testing, regressions, and latency tracking.
