<div align="center">
  <img src="assets/banner.svg" alt="Premedice 4 — medical reasoning model" width="100%" />
</div>

<h1 align="center">Premedice 4</h1>

<p align="center">
  <strong>A medical reasoning model.</strong><br/>
  Earlier warning tracking. Cited answers. Whole-record context.
</p>

<p align="center">
  <a href="https://premedice.com">Premedice</a> ·
  <a href="https://api.premedice.com">API</a> ·
  <a href="https://premedice.com/doctors/">For clinicians</a> ·
  <a href="https://github.com/Pakakothaproject/premedice">App overview</a>
</p>

<p align="center">
  <img alt="Status: beta" src="https://img.shields.io/badge/status-beta-00C853" />
  <img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-blue" />
  <img alt="Output: cited answers" src="https://img.shields.io/badge/output-cited%20answers-0B0B0B" />
</p>

---

## What Premedice 4 delivers

Premedice 4 is a **proprietary medical reasoning model** built and operated by Premedice.

It is designed for the moment a short appointment cannot cover: the small changes across labs, medicines, symptoms and history that are easy to miss, and the evidence a patient or clinician needs to act on them.

**Results you get:**

- **Earlier warning tracking** across labs, medicines, symptoms and history.
- **Cited answers** with sources attached.
- **Whole-record context** for patients, caregivers and clinicians.
- **Clinician-ready summaries** built from the active record.
- **Plain-language explanations** of labs, medicines and reports.
- **One API** for chat, lab interpretation and evidence verification.

---

## What it is used for

- Understanding a lab report in the context of the whole record.
- Spotting a meaningful change between visits.
- Reviewing medicines, interactions and pharmacogenomic notes.
- Preparing a focused summary for a clinician.
- Researching a condition, guideline or trial with citations.
- Building patient-education and clinical-support products.

---

## Coverage

| Area | Available |
|---|---|
| Clinical data sources | 45+ live sources and tools |
| Clinical skills | 76 active skills |
| Lab markers | 54 common markers with trends and reference checks |
| Output | Cited answers with uncertainty language |
| Access | Web app, OpenAI-compatible API, MCP |
| Records | Labs, medicines, documents, symptoms, timeline, notes |

---

## API

```bash
curl https://api.premedice.com/v1/chat/completions \
  -H "Authorization: Bearer pm_live_YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Premedice/Premed-4",
    "messages": [
      {"role": "user", "content": "Review these labs in the context of the patient's current medications and flag what should be discussed with a clinician."}
    ]
  }'
```

OpenAI-compatible request and streaming shape.

See the [API documentation](docs/api.md).

---

## Safety boundaries

- Premedice is decision support, not a diagnosis.
- It does not replace a licensed clinician.
- Emergency symptoms require local emergency services.

---

## Documentation

- [What Premedice 4 delivers](docs/results.md)
- [Benchmark comparison](docs/comparison.md)`n- [Model card](docs/model-card.md)
- [Safety](docs/safety.md)
- [API](docs/api.md)
- [Security policy](SECURITY.md)
- [Changelog](CHANGELOG.md)
- [Citation](CITATION.cff)

---

## License

MIT for this repository's documentation. The Premedice name, logo and product marks remain the property of Diagnostics AI, Inc.

See [LICENSE](LICENSE).
