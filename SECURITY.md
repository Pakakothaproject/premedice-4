# Security Policy

**Last updated:** 3 November 2026

---

## Reporting a vulnerability

Please use GitHub's private vulnerability reporting for this repository. Do not open a public issue for a security problem.

Include:

- affected endpoint or component
- reproduction steps
- impact
- whether PHI or credentials may be exposed
- a redacted request or response if useful

Do not include:

- live API keys
- patient identifiers
- full patient records
- production database dumps

## Scope

In scope:

- authentication and API-key handling
- cross-context or cross-patient data access
- doctor-link scope, expiry, or revocation failures
- prompt injection that changes tool behavior
- PHI appearing in logs
- evidence or citation spoofing
- unsafe emergency handling

## Out of scope

- medical disagreement without a reproducible safety issue
- missing features
- rate-limit thresholds
- issues that require a compromised device or account
- social engineering

## Disclosure

We will acknowledge a report, investigate it, and coordinate disclosure after a fix is available. Do not publish exploit details before coordination.

## Safety reports

This repository is for the Premedice 4 model card and documentation. Product safety concerns that are not security vulnerabilities should be described without patient identifiers.
