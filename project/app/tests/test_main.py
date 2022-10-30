# project/tests/test_main.py

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_fibonacci():
    response = client.get("/api/v1/algorithms/fibonacci/10")
    assert response.status_code == 200
    assert response.json() == {"result": 55}


def test_get_ackermann():
    response = client.get("/api/v1/algorithms/ackermann/1/2")
    assert response.status_code == 200
    assert response.json() == {"result": 4}


def test_get_factorial():
    response = client.get("/api/v1/algorithms/factorial/5")
    assert response.status_code == 200
    assert response.json() == {"result": 120}


def test_check_heartbeat():
    response = client.get("/api/v1/heartbeat")
    assert response.status_code == 200
    assert response.json() == ["ok"]
