# Premedice 4 — Structural Evaluation Report

**Date:**
**Model ID:**
**API base URL:**
**Case file:**
**Runner commit:**

---

## Scope

This report covers structural behavior only:

- HTTP success
- non-empty answers
- source presence
- emergency language
- uncertainty language
- disclaimer language
- latency

It does **not** cover clinical correctness, citation precision, red-flag recall, or unsupported-claim rate. Those require the clinician-adjudicated protocol in `../docs/evaluation.md`.

---

## Results

| Metric | Value |
|---|---:|
| Cases |  |
| Passed |  |
| Failed |  |
| HTTP errors |  |
| Latency min |  |
| Latency median |  |
| Latency max |  |

---

## Failures

| Case | Category | Status | Failed check | Notes |
|---|---|---|---:|---|
|  |  |  |  |  |

---

## Observations

-
-
-

---

## What this does not prove

- That the medical content is correct.
- That citations support their claims.
- That red flags are reliably detected.
- That the model is safe for clinical use.
- That the model is better than another product.

---

## Next step

Run the clinician-adjudicated protocol in `../docs/evaluation.md`. Do not publish a clinical accuracy claim from this structural report.
