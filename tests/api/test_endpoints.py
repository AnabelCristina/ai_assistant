from fastapi.testclient import TestClient
import pytest
from main import app

client = TestClient(app)

def test_health_check(test_client):
    response = test_client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK", "message": "Works"}

@pytest.mark.asyncio
async def test_question_endpoint(test_client):

    payload = {"question": "Qual a melhor ração para gatos filhotes?"}
    response = test_client.post(
        "/api/question-and-answer",
        json=payload
    )
    assert response.status_code == 200
