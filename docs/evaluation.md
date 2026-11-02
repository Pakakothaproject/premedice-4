# Premedice 4 — Clinical Evaluation Protocol

**Status:** Protocol v0.1 — no results published
**Last updated:** 3 November 2026
**Owner:** Premedice clinical evaluation workstream (lead to be named)
**Model ID:** `Premedice/Premed-4`

---

## 1. Purpose

This document defines how Premedice 4 will be evaluated before any accuracy claim is made.

It is a protocol, not a results page. No clinical accuracy claim is valid until results are published with the test set, adjudication method, and limitations.

---

## 2. Questions

The evaluation is designed to answer:

1. Are cited claims supported by the cited source?
2. Are urgent red flags recognized and escalated?
3. When sources are missing or weak, does the system say so?
4. How often does the system make an unsupported clinical claim?
5. How accurately does the system map and trend laboratory results?
6. How long does a request take, and how often does it fail?
7. Where does performance differ by case type, language, or record completeness?

---

## 3. Design

**Type:** retrospective, de-identified, clinician-adjudicated evaluation.

**Unit of analysis:** one clinical question and one Premedice response.

**Target sample:** 200–300 cases. If fewer than 200 are available, publish the smaller denominator and label the result as preliminary.

**Case mix:** include common and high-risk cases:

- lab interpretation and longitudinal change
- medication safety and interactions
- guideline-based management questions
- red-flag and emergency presentations
- rare-disease and diagnostic-odyssey cases
- cases with missing or conflicting data
- patient-facing and clinician-facing phrasing
- at least two languages if multilingual claims are made

**Exclusions:** cases with unresolved identity, incomplete consent, or data that cannot be de-identified.

---

## 4. Reference standard

Each case requires a clinician-authored reference containing:

- the key findings
- the expected red flags
- the expected sources or source types
- the acceptable answer boundary
- the “not established” items
- any case-specific safety concern

Where clinicians disagree, use a third adjudicator and record the disagreement.

---

## 5. Adjudication

- At least two independent clinicians review each case.
- Reviewers must not be Premedice employees.
- Conflicts of interest are disclosed.
- Reviewers score without seeing model identity or vendor branding where feasible.
- Disagreements are resolved by a third reviewer.
- The adjudication form and instructions are published with the results.

---

## 6. Metrics

### Primary

- **Citation precision:** proportion of cited claims supported by the cited source.
- **Red-flag recall:** proportion of clinician-identified urgent red flags that the answer escalates.
- **Unsupported-claim rate:** proportion of clinical claims with no supporting source or explicit uncertainty.
- **Lab mapping accuracy:** proportion of lab values correctly mapped to analyte, unit, and reference range.

### Secondary

- refusal correctness on out-of-scope or unsafe requests
- “not established” correctness when evidence is missing
- time to first token and total latency
- tool failure rate
- source freshness and source quality
- cross-context leakage rate (must be zero)
- clinician-rated usefulness
- patient-readable clarity

### Safety

Any cross-context leakage, missed emergency escalation, or unsafe prescribing recommendation is a critical failure and is reported individually, not averaged away.

---

## 7. Analysis

- Report numerators and denominators for every metric.
- Report confidence intervals where the sample supports them.
- Report results by case type and language.
- Report failures, not only successes.
- Do not compare against another product unless that product was evaluated on the same cases with the same adjudication.
- Do not republish a third-party benchmark as a Premedice result.

---

## 8. Publication

The results package will include:

1. This protocol, with any amendments and dates.
2. The de-identified case set or a reproducible sampling description.
3. The adjudication form and reviewer instructions.
4. Per-case scores or aggregate tables.
5. Failure examples, with consent and redaction.
6. Limitations and conflicts of interest.
7. A statement of what the evaluation does **not** prove.

---

## 9. What this evaluation will not prove

- That Premedice improves patient outcomes.
- That Premedice is safer than a clinician.
- That Premedice is a medical device or is cleared for diagnosis.
- That results generalize to every population, language, or care setting.
- That a single evaluation is enough for clinical adoption.

Those claims require prospective studies, regulatory review, and post-market monitoring.

---

## 10. Current status

| Item | Status |
|---|---|
| Protocol | Drafted |
| Case set | Not assembled |
| Clinical reviewers | Not recruited |
| Adjudication | Not started |
| Results | Not published |
| External validation | Not started |

Until the table above changes, Premedice 4 has **no published clinical accuracy result**.
