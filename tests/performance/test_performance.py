import time

def test_response_time(test_client):
    payload = {"question": "teste de performance"}
    
    start = time.time()
    response = test_client.post("/api/question-and-answer", json=payload)
    elapsed = time.time() - start

    assert response.status_code == 200
    assert elapsed < 2.5  