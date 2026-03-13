from fastapi.testclient import TestClient

from api.server import create_app


client = TestClient(create_app())


def test_healthcheck() -> None:
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_call_simulation() -> None:
    response = client.post(
        "/api/v1/simulate/call",
        json={"caller": "+12025550100", "callee": "+12025550101"},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "established"
    assert len(body["timeline"]) == 5
