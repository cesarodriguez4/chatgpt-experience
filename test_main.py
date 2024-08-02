from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"chatgpt-experience": "ready"}

def test_chatgpt_query():
    response = client.post("/chatgpt-query", json={"query": "Hello, how are you?"})
    assert response.status_code == 200
    assert response.json().get("response") is not None