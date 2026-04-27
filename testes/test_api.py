from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Olá mundo"}

def test_soma():
    response = client.get("/soma/2/3")
    assert response.status_code == 200
    assert response.json() == {"resultado": 5}