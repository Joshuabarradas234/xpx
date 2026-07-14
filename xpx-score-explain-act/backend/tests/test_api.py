"""API tests for the Score -> Explain -> Act engine.

Run from the backend/ directory:  pytest
"""
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_ok():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_low_risk_request_is_approved():
    payload = {
        "amount": 300,
        "employer": "XP Demo Employer",
        "pay_frequency": "monthly",
        "tenure_months": 36,
        "repayment_history_score": 800,
    }
    resp = client.post("/score", params={"mode": "RULES_ONLY"}, json=payload)
    assert resp.status_code == 200
    body = resp.json()
    assert body["risk_band"] == "Green"
    assert body["recommended_action"] == "Approve"
    assert len(body["top_drivers"]) == 3
    assert body["policy_citation"].startswith("Policy PX-ADV-01")


def test_high_risk_request_is_declined_and_has_ml_score():
    payload = {
        "amount": 4500,
        "employer": "XP Demo Employer",
        "pay_frequency": "weekly",
        "tenure_months": 1,
        "repayment_history_score": 500,
    }
    resp = client.post("/score", params={"mode": "ML_PLUS_RULES"}, json=payload)
    assert resp.status_code == 200
    body = resp.json()
    assert body["risk_band"] == "Red"
    assert body["ml_score"] is not None


def test_invalid_request_is_rejected():
    resp = client.post("/score", json={"amount": -5})
    assert resp.status_code == 422
