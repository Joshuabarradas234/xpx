# Backend — Score → Explain → Act API

A FastAPI service that scores a salary-advance request and returns an explainable,
policy-cited decision.

## Endpoints
- `GET /health` — liveness check → `{ "status": "ok" }`
- `POST /score?mode=RULES_ONLY|ML_PLUS_RULES` — score a request

## How scoring works
`app/main.py` contains the whole service:
- `rules_score()` — deterministic business rules over amount, tenure, repayment history,
  and pay frequency; produces a 0–100 score and human-readable drivers.
- `ml_score()` — a transparent deterministic stub returning a 0–1 adverse-outcome signal
  (placeholder for a trained model; see ADR-0001).
- `band_and_action()` — maps the score to Green/Amber/Red and Approve/Review/Decline.
- `POST /score` blends rules + model signal (60/40) in `ML_PLUS_RULES` mode and attaches
  the top drivers and a policy citation.

## Run
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```
Swagger UI: http://127.0.0.1:8000/docs

## Test
```bash
pip install -r requirements-dev.txt
pytest
```

## Layout
```
backend/
├── app/
│   ├── __init__.py
│   └── main.py            # FastAPI app: schemas, rules, model-stub, endpoints
├── tests/
│   └── test_api.py        # /health + /score (low/high risk + validation)
├── requirements.txt
├── requirements-dev.txt
└── Dockerfile
```
