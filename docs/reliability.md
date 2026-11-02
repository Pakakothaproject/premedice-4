# Premedice 4 — Reliability and Latency

**Status:** Preview
**Last updated:** 3 November 2026

---

## Current status

Premedice 4 is in preview. There is no public uptime SLA and no public latency SLA.

## What is measured today

- API responses return request metadata where available.
- The system records first-token and total-request timing internally.
- Individual tool calls can fail without failing the whole answer.
- Rate limits apply per API key.

## What is not yet published

- p50/p95/p99 latency
- uptime
- error rate
- tool failure rate
- cost per answer
- timeout rate
- regional availability

These will be published only after they are measured on a defined workload.

## Known behavior

- Simple questions are faster than multi-tool clinical requests.
- Complex requests can take tens of seconds.
- Retrieval or verification can time out.
- The verifier can fail open rather than block an answer.
- The API can return a partial answer when a tool fails.
- No retry or idempotency guarantee is published.

## Recommended client behavior

- Set a client timeout.
- Retry only idempotent reads.
- Do not retry a request that may have already been billed without checking usage.
- Show a loading state; do not assume sub-second responses.
- Treat a missing source as a reason to verify, not a reason to trust.

## Reliability claims

Do not publish an SLA, uptime percentage, or latency guarantee until there is a measured workload and a public status page. This page will be updated when those exist.
