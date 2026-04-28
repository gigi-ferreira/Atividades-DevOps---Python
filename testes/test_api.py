from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_gatinho_soninho():
    response = client.get("/gatinho/cafe")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("image/")
    assert len(response.content) > 0

def test_gatinho_gatao():
    response = client.get("/gatinho/gatao")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("image/")
    assert len(response.content) > 0

def test_fome_elevada():
    response = client.get("/fome/8")
    assert response.status_code == 200
    assert "muita fome" in response.json()["status"]

def test_fome_invalida():
    response = client.get("/fome/20")
    assert response.status_code == 400
    assert response.json()["detail"] == "O nivel de fome deve ser entre 0 e 10"

def test_fome_nivel_negativo():
    response = client.get("/fome/-1")
    assert response.status_code == 400
    assert response.json()["detail"] == "O nivel de fome deve ser entre 0 e 10"
