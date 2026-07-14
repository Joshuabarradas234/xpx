# ADR-0001 — Hybrid rules + model scoring

**Status:** Accepted

## Context
Salary-advance decisions must be both flexible and defensible. A pure model is hard to
audit and explain; a pure rules engine is transparent but rigid and hard to tune.

## Decision
Combine deterministic business rules with a model-style signal. In `ML_PLUS_RULES` mode
the final score is a weighted blend (60% rules / 40% model signal); `RULES_ONLY` mode
returns the rules score alone. Every response carries top drivers and a policy citation.

The model signal is currently a transparent deterministic stub. This keeps the demo fully
reproducible while proving the blend mechanics; replacing it with a trained model
(e.g. GBDT) does not change the API contract.

## Consequences
- Decisions are explainable and auditable by construction.
- Rules and model are independently testable and swappable.
- Trade-off: the stub is not predictive on its own — it exists to exercise the pipeline,
  not to make real credit decisions.

## Alternatives considered
- Fully ML-driven scoring (rejected: weak auditability for a regulated flow).
- Fully rule-based engine (rejected: no path to a learned model later).
