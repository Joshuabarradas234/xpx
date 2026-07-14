# Architecture

![Architecture](architecture/xpx-architecture.png)

## Overview

This is an Azure-native reference architecture for an explainable salary-advance /
instant-pay risk engine: GDPR-first, EU-hosted, and built on **synthetic data only**
(no real PII). It is the *target production design*. The code in this repository
implements the decisioning core (Layers 3–4) so the Score → Explain → Act flow can be
run and demonstrated locally; the surrounding platform is designed, not deployed.

Legend used in the diagram: **left (blue)** = what each layer does · **centre (icons)**
= how it works (services + flow) · **right (yellow)** = outputs. Thick arrows are the
primary data flow; the dashed grey loop is the MLOps feedback path
(telemetry → drift → retrain → redeploy).

## Layers

**Layer 1 — Data (synthetic inputs).** Synthetic employee profiles, advance requests,
repayment outcomes, public regulations/policies, and product metadata. This keeps the
whole system free of real personal data while still exercising realistic decision logic.
The regulations/policies input is what makes "GDPR-first" concrete rather than a slogan.

**Layer 2 — Storage (governed).** ADLS Gen2 raw → curated zones, versioned Delta/Parquet
feature tables, with Purview/Fabric providing lineage, governance, and dataset discovery.
Output: curated, feature-ready tables plus lineage.

**Layer 3 — Offline ML (build/train).** ADF/Synapse ingestion, Databricks/Spark feature
engineering, a feature store, an interpretable risk model (e.g. GBDT), an anomaly model,
SHAP-based explainability, a model registry, and CI/CD. Output: versioned features,
risk/anomaly models, explainability reports, and registered artifacts.
*Implemented here as a transparent rules + model-stub scorer with driver-level explanations.*

**Layer 4 — Online serving (real-time scoring).** A managed online endpoint fronted by a
policy/rules engine and a scoring API, with an optional cache for low latency. It returns
a risk band, the drivers, an anomaly signal, and a recommended action — not just a number.
*This is the `POST /score` endpoint implemented in `backend/app/main.py`.*

**Layer 5 — Product (surfaces).** Employee app (advance request + explainable risk
indicator), employer/HR manager views (risk + cashflow dashboards, alerts), and a
prototype demo surface. *Implemented here as the React + Vite frontend.*

**Layer 6 — Ops/Sec.** Identity (Azure AD), least-privilege RBAC + managed identity,
Key Vault, monitoring (App Insights), model monitoring (drift + fairness), VNet + private
endpoints, and immutable audit logs. Output: audit trail, monitoring dashboards, and
drift/fairness checks.

## What the running code covers

| Diagram layer | In this repo |
| --- | --- |
| Layer 3 — offline ML | Rules + model-stub scorer with explainable drivers |
| Layer 4 — online serving | `GET /health`, `POST /score` (FastAPI) + policy citation |
| Layer 5 — product | React + Vite UI |

## The design decision I kept coming back to

Explainability. It is easy to list SHAP on a slide; the harder part is making an
explanation survive a real-time API call — a risk band, the top drivers, and a
recommended action returned in one response that a person can actually read and a
reviewer can audit. That contract is what this repo demonstrates, and it is why the
scoring and the explanation are deliberately kept separate and deterministic.
