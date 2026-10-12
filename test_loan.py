import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.mimetype == "text/html"

    html = response.get_data(as_text=True)
    assert "<title>Loan Eligibility Prediction App</title>" in html
    assert '<form action="/predict" method="POST">' in html
    assert 'name="income"' in html


def test_predict_rejects_large_loan(client):
    data = {
        "income": 20000,
        "credit_score": 500,
        "loan_amount": 1000000,
        "employment_status": 0,
    }
    response = client.post("/predict", data=data)

    assert response.status_code == 200
    assert response.mimetype == "text/html"

    html = response.get_data(as_text=True)
    assert "REJECTED" in html
    assert 'class="alert mt-4 text-center alert-danger"' in html


def test_predict_approves_low_amount(client):
    data = {
        "income": 80000,
        "credit_score": 750,
        "loan_amount": 10000,
        "employment_status": 1,
    }
    response = client.post("/predict", data=data)

    assert response.status_code == 200
    assert response.mimetype == "text/html"

    html = response.get_data(as_text=True)
    assert "APPROVED" in html
    assert 'class="alert mt-4 text-center alert-success"' in html