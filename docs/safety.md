# Premedice 4 — Safety

**Status:** Preview
**Last updated:** 3 November 2026

---

## 1. Intended use

Premedice 4 is an information and decision-support tool. It is not a medical device, not a diagnosis, and not a substitute for a licensed clinician.

## 2. Emergency use

Premedice must not be used for emergency triage or emergency care.

If a person has chest pain, stroke symptoms, severe bleeding, anaphylaxis, difficulty breathing, loss of consciousness, or suicidal thoughts, they should contact local emergency services or a crisis line immediately.

## 3. No autonomous diagnosis or prescribing

Premedice must not:

- issue a definitive diagnosis
- authorize a prescription
- set or change a dose
- order treatment
- replace a clinician's sign-off

Any clinical action requires a licensed professional who has reviewed the source evidence and the patient's full context.

## 4. Evidence checks are not guarantees

Premedice uses a post-answer verification pass. It can:

- time out
- fail open
- miss a red flag
- accept a weak source
- show a warning without changing the main answer

A missing warning is not proof that an answer is safe.

## 5. Doctor sharing

A shared record is not a clinical endorsement. Doctor accounts are invitation-based and scoped, but professional-email verification and signed review are still being expanded. Do not treat an unverified account as a verified clinician.

## 6. Data safety

- Do not submit PHI to a deployment without an appropriate agreement.
- Do not put PHI in GitHub issues, pull requests, or discussions.
- Do not paste patient records into public evaluation cases.
- Report a vulnerability through GitHub private vulnerability reporting; see [SECURITY.md](../SECURITY.md).

## 7. Reporting a safety problem

For a product safety issue, include:

- the model ID
- the request type
- whether a red flag was missed
- whether a source was wrong
- whether the issue is reproducible
- a redacted example

Do not include patient identifiers.

## 8. Safety claims

No safety claim is valid without a published evaluation. The current evaluation protocol is in [evaluation.md](evaluation.md). The current limitations are in [limitations.md](limitations.md).
