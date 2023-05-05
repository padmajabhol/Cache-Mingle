from fastapi.testclient import TestClient
from main import app
import json

client = TestClient(app)

data = {
    "key": "1",
    "value": "padmaja"
}

def test_create_value():
    response = client.put("/cache/1", json=data)
    assert response.status_code == 200
    assert response.json() == data

def test_get_value():
    response = client.get("/cache/1")
    assert response.status_code == 200
    assert response.json() == data

def test_view_keys():
    response = client.get("/caches/keys")
    assert response.status_code == 200
    assert response.json() == {"keys": list(data["key"])}

def test_get_entire_cache():
    response = client.get("/cache")
    assert response.status_code == 200
    assert response.json() == {'value': {data["key"]: data["value"]}}

def test_delete():
    response = client.delete("/cache/1")
    assert response.status_code == 200
    assert response.json() == {'data': "value is deleted"}

# data_bulk = {"key": "1",
#              "value": "padmaja"}
    
# def test_set_bulk_value():
#     response = client.put("/bulkvalue", json=data)
#     assert response.status_code == 200
#     assert response.json() == {'message': "Set successfully"}

def test_set_bulk_value():
    key1, value1 = "key1", "value1"
    key2, value2 = "key2", "value2"
    key3, value3 = "key3", "value3"
    request_body = {
        "items": [
            {"key": key1, "value": value1},
            {"key": key2, "value": value2},
            {"key": key3, "value": value3},
        ]
    }

    # Make a request to the set_bulk_value endpoint
    response = client.put("/bulkcache", json=request_body)

    # Assert that the response status code is 200
    assert response.status_code == 200
    assert response.json() == {'message': 'Set successfully'}

def test_get_cache_values():
    key1, value1 = "key1", "value1"
    key2, value2 = "key2", "value2"
    key3, value3 = "key3", "value3"
    request_body = {"keys": [key1, key2, key3]}
    response = client.get("/bulkcache", params={"keys": ["key1", "key2", "key3"]})
    assert response.status_code == 200
    assert response.json() == {"values": {key1: value1, key2: value2, key3: value3}}

def test_delete_bulk():
    # key1 = "key1"
    # key2 = "key2"
    # key3 = "key3"
    # request_body = {"keys": [key1, key2, key3]}
    response = client.delete("/bulkcache", params={"keys": ["key1", "key2", "key3"]})
    assert response.status_code == 200

data1 = {
    "maxsize": 256,
    "ttl": 300
}
def test_configure_cache():
    response = client.put("/configure", json=data1)
    assert response.status_code == 200
    assert response.json() == {"data": f"new maxsize set to {data1['maxsize']} and ttl set to {data1['ttl']}"}


