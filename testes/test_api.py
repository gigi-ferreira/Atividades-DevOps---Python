from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_gatinho_soninho():
    response = client.get("/gatinho/soninho")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("image/")
    assert len(response.content) > 0

def test_gatinho_gatao():
    response = client.get("/gatinho/gatao")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("image/")
    assert len(response.content) > 0