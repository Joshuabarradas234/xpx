# ADR-0002 — Synthetic data only

**Status:** Accepted

## Context
This is a portfolio demo of a system that would, in production, handle sensitive
employment and financial data under GDPR.

## Decision
Use synthetic inputs exclusively — no real personal or financial data enters the system
at any layer. Configuration and any secrets are supplied via environment variables and
kept out of version control.

## Consequences
- Zero PII risk; the repo is safe to share publicly.
- The GDPR-first production design (EU hosting, private endpoints, audit logs) can be
  documented as intent without exposing real data.
- Trade-off: results are illustrative and not validated against real-world outcomes.
