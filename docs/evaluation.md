# Premedice 4 — Clinical Evaluation Protocol

**Status:** Protocol and harness ready. Results are published only after clinician adjudication.

---

## Goal

Measure whether Premedice 4:

1. cites sources that support its claims
2. catches urgent red flags
3. says when evidence is missing or weak
4. avoids unsupported clinical claims
5. returns answers within a usable latency

## Design

- 100–300 de-identified cases.
- At least two independent clinician reviewers.
- A third reviewer resolves disagreements.
- A clinician-authored reference standard for every case.
- Cases cover labs, medicines, guidelines, emergencies, rare disease, missing data, and patient education.
- Published results include numerators, denominators, failures, and limitations.

## Harness

- [Case schema](../evaluation/cases.schema.json)
- [Example synthetic cases](../evaluation/cases.example.jsonl)
- [Answer collector](../evaluation/run_cases.py)
- [Clinical scorer](../evaluation/score_clinical.py)
- [Adjudication template](../evaluation/adjudication.template.csv)
- [Report template](../evaluation/REPORT_TEMPLATE.md)

## Metrics

Primary:

- citation precision
- red-flag recall
- unsupported-claim rate
- adjudication coverage

Secondary:

- latency p50/p95
- per-category performance
- refusal correctness
- source quality

## Publication

A result is publishable only when:

- at least 100 cases are adjudicated, or the smaller denominator is clearly labelled
- reviewer disagreements are reported
- failures are included
- the case set or sampling method is described
- the report states what the evaluation does not prove

## What this does not prove

- improved patient outcomes
- regulatory clearance
- superiority to a clinician
- performance outside the tested case mix
