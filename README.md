
```markdown
# XPX — Score → Explain → Act

### Explainable salary-advance risk decisioning — designed & prototyped for XPX Technologies under contract

![status](https://img.shields.io/badge/status-demo-blue)
![backend](https://img.shields.io/badge/backend-FastAPI-009688)
![frontend](https://img.shields.io/badge/frontend-React%20%2B%20Vite-646CFF)
![tests](https://img.shields.io/badge/tests-pytest-brightgreen)
![CI](https://github.com/Joshuabarradas234/xpx/actions/workflows/ci.yml/badge.svg)
![license](https://img.shields.io/badge/license-MIT-lightgrey)

> Cloud engineering contract for **XPX Technologies** (Leeds instant-pay fintech), Nov 2025 – Apr 2026.
> I was engaged to design the target architecture and build a working prototype of the scoring core.
> Published with XPX's permission. All data in this repository is synthetic — no real client data or PII.

> Submit a salary-advance request → get a **risk score**, see **why** (top drivers + the policy that fired), and receive a **recommended action** (Approve / Review / Decline).

---

## What it is

A small, full-stack **risk-decisioning engine** that mirrors how fintech / payroll / lending systems turn an application into an *auditable* decision instead of an opaque score:

1. **Score** — a hybrid of deterministic business rules and a model signal produces a risk band (Green / Amber / Red).
2. **Explain** — the response returns the top drivers behind the score and the specific policy rule that fired.
3. **Act** — a recommended action (Approve / Review / Decline), not just a number.

The scoring core is built and runnable. The wider platform around it (cloud storage, offline ML training, real-time serving, ops) is **designed, not deployed** — see the status table below.

---

## Implementation status (what's real vs. designed)

| Area | Status |
|---|---|
| `/health` and `/score` API (FastAPI) | ✅ Implemented |
| Hybrid rules + model-signal scoring, risk banding | ✅ Implemented |
| Explainability — top drivers + policy citation in response | ✅ Implemented |
| React + Vite frontend (request → score → explanation) | ✅ Implemented |
| pytest suite, Dockerfiles, docker-compose, CI workflow | ✅ Implemented |
| Trained ML model (the current model signal is a stub) | 🎯 Roadmap |
| Anomaly detection, SHAP explainability | 🎯 Roadmap |
| RAG-grounded policy retrieval | 🎯 Roadmap |
| Azure platform (ADLS, Azure ML, online endpoint, ops/sec) | 📐 Designed, not deployed |

Legend: ✅ built and runnable · 🎯 planned next step · 📐 designed in the architecture, not implemented here.

---

## Architecture (designed)

The target architecture is a six-layer, GDPR-first design: synthetic-data ingestion → governed storage with lineage → offline ML (risk model + anomaly detection + SHAP explainability) → real-time scoring API → employee/employer surfaces → an ops layer covering drift monitoring, fairness checks and immutable audit logs.

This is the **design deliverable** from the engagement. The diagram lives in [`docs/architecture/`](docs/architecture). The code in this repository implements the scoring core at the centre of it, not the full platform.

---

## Run it locally

```bash
# Backend
cd backend
pip install -r requirements-dev.txt
uvicorn app.main:app --reload   # http://127.0.0.1:8000

# Frontend
cd frontend
npm install
npm run dev                     # http://localhost:5173
```

The frontend reads the API base URL from `VITE_API_BASE` (see `frontend/.env.example`); it defaults to `http://127.0.0.1:8000`.

Or run both with Docker:

```bash
docker compose up --build
```

---

## Tests & CI

```bash
cd backend
pytest -q
```

GitHub Actions runs the backend (ruff + pytest) and frontend (eslint + build) on every push and pull request — see the CI badge above.

---

## Evidence

Screenshots of the running prototype are in [`docs/screenshots/`](docs/screenshots):

| # | File | Shows |
|---|------|-------|
| 06 | `06-frontend-decision.png` | Frontend: request → risk band + explanation |
| 07 | `07-score-response.png` | `/score` API response with drivers and policy citation |
| 09 | `09-tests-passing.png` | pytest suite passing |

---

## Security & data notes

- All data in this repository is **synthetic** — no real client data, no PII.
- No secrets in code — configuration is via environment variables (`.env` is git-ignored; see `frontend/.env.example`).
- Least-privilege access, Key Vault, private endpoints and immutable audit logging are part of the **designed** Azure architecture, not implemented in this prototype.

---

## Repository structure

```
xpx/
├── backend/          # FastAPI service + pytest
├── frontend/         # React + Vite UI
├── docs/             # architecture, ADRs, screenshots
├── docker-compose.yml
└── .github/workflows/ci.yml
```

---

## License

MIT — see [LICENSE](LICENSE).
```

**Two things before you commit:**

1. **Check the evidence table against your actual filenames.** I listed screenshots 06, 07, 09 — the ones your original index referenced. If your real files are named differently, adjust that table to match, and list whichever screenshots genuinely exist (minus 10). If you're not sure, open `docs/screenshots/` and tell me the filenames and I'll fix the table exactly.

2. **You still need to delete the image file** `docs/screenshots/10-env-configuration.png` itself — removing its table row here doesn't delete the file. Do that as a separate step (navigate to it → ⋯ → Delete file).

Commit message: `Reframe README as XPX contract work; remove env screenshot`.

Want the recommendation draft next? For that I just need: what would the owner genuinely say the work delivered — the architecture, the prototype, both — and did it actually feed their product thinking?
