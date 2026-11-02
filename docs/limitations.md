# Premedice 4 — Limitations

**Status:** Preview
**Last updated:** 3 November 2026

This page lists known limitations. It is not a complete safety case.

---

## Clinical limitations

- Premedice does not examine the patient.
- It does not replace clinical judgment.
- It can miss diagnoses, red flags, and drug interactions.
- It can cite a source that does not fully support the claim.
- It can produce a confident answer from weak evidence.
- It can fail to ask for missing information.
- It does not provide autonomous diagnosis or prescribing.
- It is not a medical device and is not FDA-cleared or CE-marked.

## Evidence limitations

- Retrieval can fail, time out, or return weak sources.
- The verifier can time out and fail open.
- Missing red flags and contradictions may be shown in the evidence panel without changing the main answer.
- Source quality and guideline versions are not yet consistently graded.
- Citation precision and red-flag recall have not been published.

## Record limitations

- Lab parsing is strongest on clean text, not every real-world lab format.
- The analyte dictionary is incomplete.
- Critical thresholds are not yet complete.
- Backfill, deduplication, and manual correction are incomplete.
- Reference ranges are not yet localized by country or lab system.
- Cross-context isolation requires continued RLS testing.

## Doctor and sharing limitations

- Professional email is not yet verified by OTP or domain proof.
- A shared record is not a clinical endorsement.
- Signed immutable doctor review is not yet complete.
- Doctor access must be scoped, auditable, and revocable.
- A doctor account must never see an unlinked patient.

## Operational limitations

- No public uptime SLA.
- No public latency SLA.
- Complex multi-tool requests can take tens of seconds.
- Rate limits and error behavior may change during preview.
- The API can change before a stable release.

## Regulatory limitations

- FDA CDS, EU AI Act, GDPR, and local medical-device rules may apply.
- Legal and clinical governance review is required before clinical deployment.
- This repository is not a regulatory submission.

## What would remove a limitation

A limitation is removed only when there is a test, a measured result, and a public artifact that demonstrates the fix. Marketing copy alone does not remove a limitation.
