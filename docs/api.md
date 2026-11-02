# Premedice 4 — API

**Status:** Preview
**Base URL:** `https://api.premedice.com`
**Canonical model ID:** `Premedice/Premed-4`

---

## 1. Authentication

```http
Authorization: Bearer pm_live_YOUR_KEY
```

Keys are created in the Premedice dashboard. Never publish a live key.

---

## 2. Chat completions

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

The response shape follows the OpenAI Chat Completions format. The API also returns Premedice metadata when available.

---

## 3. Model list

```bash
curl https://api.premedice.com/v1/models \
  -H "Authorization: Bearer pm_live_YOUR_KEY"
```

The live model list currently advertises:

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

## 4. Lab interpretation

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

The API returns an interpretation with sources and safety flags. It does not diagnose or prescribe.

---

## 5. Evidence verification

```http
POST /v1/evidence/verify
```

Request:

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

The endpoint returns whether the claim is supported, unsupported, or requires more evidence.

---

## 6. MCP

The API exposes an MCP endpoint at:

```text
https://api.premedice.com/mcp
```

It uses the same `pm_live_*` key and is intended for other AI clients that want to delegate medical research to Premedice.

---

## 7. Preview limits

- No public uptime SLA.
- No public latency SLA.
- Rate limits and response fields may change.
- The API is decision support, not a diagnosis.
- Do not use it for emergency care.
- Do not send PHI unless the deployment has an appropriate agreement.

See [reliability.md](reliability.md) and [limitations.md](limitations.md).
