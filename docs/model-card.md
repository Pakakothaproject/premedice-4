# Premedice 4 — Model Card

**Status:** Beta
**Last updated:** 3 November 2026
**Model ID:** `Premedice/Premed-4`
**Provider:** Premedice
**License:** MIT for this model card and documentation

---

## 1. Summary

Premedice 4 is a proprietary medical reasoning model built and operated by Premedice.

It is designed for whole-record medical reasoning: reading labs, medicines, documents, symptoms and history together, then returning a cited answer that a patient or clinician can act on.

Its focus is earlier warning tracking — the small changes that are easy to miss when care is split across short visits, different clinicians and scattered records.

---

## 2. What it delivers

- Earlier warning tracking across labs, medicines, symptoms and history.
- Cited answers with sources attached.
- Whole-record context for patients, caregivers and clinicians.
- Plain-language explanations of lab results, medicines and reports.
- Clinician-ready summaries built from the active record.
- Drug-interaction and pharmacogenomic review.
- Guideline, trial and literature lookup with citations.
- Rare-disease phenotype matching.
- One OpenAI-compatible model identifier.

---

## 3. Intended use

Premedice 4 is intended for:

- patient and caregiver education
- clinical decision support
- lab and document interpretation
- medication and pharmacogenomic review
- guideline and trial research
- clinician-ready summaries
- patient-education drafts
- medical research workflows

It is designed to support a licensed clinician, not replace one.

---

## 4. Coverage

| Area | Available |
|---|---|
| Clinical data sources | 45+ live sources and tools |
| Clinical skills | 76 active skills |
| Lab markers | 54 common markers with trends and reference checks |
| Output | Cited answers with uncertainty language |
| Access | Web app, OpenAI-compatible API, MCP |
| Records | Labs, medicines, documents, symptoms, timeline, notes |

---

## 5. Inputs and outputs

**Input:** text, optional patient-record context, and an OpenAI-compatible messages array.

**Output:** text with citations, uncertainty language, and source metadata where available.

---

## 6. API

```bash
curl https://api.premedice.com/v1/chat/completions \
  -H "Authorization: Bearer pm_live_YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Premedice/Premed-4",
    "messages": [
      {"role": "user", "content": "Review these labs in the context of the current medications and flag what should be discussed with a clinician."}
    ]
  }'
```

The API is OpenAI-compatible. See [api.md](api.md).

---

## 7. Safety boundaries

- Premedice is decision support, not a diagnosis.
- It does not replace a licensed clinician.
- Emergency symptoms require local emergency services.
- Clinical decisions remain with a qualified professional who knows the patient.

---

## 8. Citation

If you refer to this model card, cite:

> Premedice. *Premedice 4 — Model Card.* Beta, 3 November 2026. https://github.com/Pakakothaproject/premedice-4

A machine-readable citation is available in [CITATION.cff](../CITATION.cff).
