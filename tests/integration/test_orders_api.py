from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_order():
    response = client.post("/orders", json={
        "product": "book",
        "price": 10
    })

    assert response.status_code == 201
    data = response.json()

    assert data["product"] == "book"
    assert data["price"] == 10
