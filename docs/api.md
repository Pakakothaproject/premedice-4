# Premedice 4 — API

**Status:** Beta
**Base URL:** `https://api.premedice.com`
**Model ID:** `Premedice/Premed-4`

---

## Authentication

```http
Authorization: Bearer pm_live_YOUR_KEY
```

Keys are created in the Premedice dashboard. Keep live keys private.

---

## Chat completions

```bash
curl https://api.premedice.com/v1/chat/completions \
  -H "Authorization: Bearer pm_live_YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Premedice/Premed-4",
    "messages": [
      {
        "role": "user",
        "content": "Review these labs in the context of the current medications and flag what should be discussed with a clinician."
      }
    ]
  }'
```

The response follows the OpenAI Chat Completions format and includes citation metadata where available.

---

## Model list

```bash
curl https://api.premedice.com/v1/models \
  -H "Authorization: Bearer pm_live_YOUR_KEY"
```

```json
{
  "object": "list",
  "data": [
    {
      "id": "Premedice/Premed-4",
      "object": "model",
      "owned_by": "premedice"
    }
  ]
}
```

---

## Lab interpretation

```bash
curl https://api.premedice.com/v1/labs/interpret \
  -H "Authorization: Bearer pm_live_YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "labs": [
      {"analyte": "eGFR", "value": 58, "unit": "mL/min/1.73m2", "collected_at": "2026-10-01"},
      {"analyte": "Creatinine", "value": 1.2, "unit": "mg/dL", "collected_at": "2026-10-01"}
    ],
    "question": "What changed and what should be discussed with a clinician?"
  }'
```

Returns an interpretation with sources and safety flags.

---

## Evidence verification

```http
POST /v1/evidence/verify
```

```json
{
  "claim": "ACE inhibitors reduce mortality in HFrEF.",
  "sources": [
    {
      "source_type": "guideline",
      "title": "2022 AHA/ACC/HFSA Heart Failure Guideline",
      "url": "https://www.ahajournals.org/"
    }
  ]
}
```

Returns whether the claim is supported, unsupported, or needs more evidence.

---

## MCP

```text
https://api.premedice.com/mcp
```

Uses the same `pm_live_*` key. Built for AI clients that want to delegate medical research to Premedice.

---

## Usage

- Use a key with the appropriate plan.
- Rate limits apply per key.
- Do not use the API for emergency care.
- Do not send PHI without an appropriate agreement.
- Clinical decisions remain with a licensed professional.

See [Safety](safety.md).
