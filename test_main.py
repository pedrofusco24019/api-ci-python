from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "API Online"}

def test_soma():
    response = client.get("/somar/10/20")
    assert response.status_code == 200
    assert response.json() == {"resultado": 30}

def test_multiplicar_erro():
    response = client.get("/multiplicar/2/2")
    assert response.json() == {"resultado": 5}
