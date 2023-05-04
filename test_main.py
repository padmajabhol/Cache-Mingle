from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

data = {
    "key": "1",
    "value": "padmaja"
}

def test_create_value():
    response = client.put("/value/1", json=data)
    assert response.status_code == 200
    assert response.json() == data

def test_get_value():
    response = client.get("/value/1")
    assert response.status_code == 200
    assert response.json() == data

def test_view_keys():
    response = client.get("/values/keys")
    assert response.status_code == 200
    assert response.json() == {"keys": list(data["key"])}

def test_delete():
    response = client.delete("/value/1")
    assert response.status_code == 200
    assert response.json() == {'data': "value is deleted"}

