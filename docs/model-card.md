# Premedice 4 — Model Card

## Model details

- **Name:** Premedice 4
- **Class:** Medical reasoning orchestrator
- **Primary reasoning model:** Gemini 4 Argon
- **Version:** preview
- **Owner:** Diagnostics AI, Inc.
- **License:** MIT for this documentation; model weights are not included.

## Intended use

Premedice 4 is intended for:

- evidence-grounded medical question answering;
- lab report and document interpretation;
- medication interaction and pharmacogenomic review;
- guideline, trial and literature retrieval;
- rare-disease phenotype matching;
- patient-education drafts;
- clinician-ready summaries.

## Out-of-scope use

- diagnosis or treatment decisions;
- replacing a licensed clinician;
- emergency or real-time monitoring;
- imaging, DICOM, ECG or signal interpretation;
- autonomous prescribing.

## Architecture

Premedice 4 composes a primary frontier reasoning model with a clinical tool router, whole-record context, and a verification pass. It is not a single end-to-end trained foundation model.

## Evaluation

Upstream Gemini 4 Argon results are published by Google DeepMind. Premedice 4 composite evaluation is in progress. No external clinical validation has been published.

## Limitations

- Source coverage varies by condition, language and recency.
- Tool results can be incomplete or inconsistent.
- Citations must be checked.
- The system can be wrong.
- Clinical judgment remains with a qualified clinician.

## Safety

- Red-flag and emergency handling are part of the product layer.
- The model is not a medical device.
- Outputs require clinician review for clinical decisions.
