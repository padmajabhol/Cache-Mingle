from fastapi.testclient import TestClient
from fastapi import status
from main import app

client = TestClient(app)

data = {
    "key": "1",
    "value": "padmaja"
}

data2 = {
    "key": " ",
    "value": "padmaja"
}

def test_create_value():
    response = client.put("/cache/1", json=data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == data
    key = " "
    assert client.put(f"/cache/{key}", json=data2).status_code == status.HTTP_404_NOT_FOUND
    assert client.put(f"/cache/{key}", json=data2).json() == {"detail": "Invalid key"}

def test_get_value():
    response = client.get("/cache/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == data
    assert client.get("/cache/2").status_code == status.HTTP_404_NOT_FOUND
    assert client.get("/cache/2").json() == {"detail": "Value with key 2 not found"}

def test_view_keys():
    response = client.get("/cache/all/keys")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"keys": [data["key"]]}

def test_get_entire_cache():
    response = client.get("/cache")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'data': {data["key"]: data["value"]}}

def test_delete():
    response = client.delete("/cache/1")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert client.get("/cache/1").status_code == 404

def test_set_bulk_value():
    key1, value1 = "key1", "value1"
    key2, value2 = "key2", "value2"
    key3, value3 = "key3", "value3"
    key4, value4 = " ", "value4"
    request_body = {
        "items": [
            {"key": key1, "value": value1},
            {"key": key2, "value": value2},
            {"key": key3, "value": value3},
        ]
    }

    request_body2 = {
        "items": [
            {"key": key1, "value": value1},
            {"key": key2, "value": value2},
            {"key": key4, "value": value4},
        ]
    }

    # Make a request to the set_bulk_value endpoint
    response = client.put("/bulkcache", json=request_body)

    # Assert that the response status code is 201
    assert response.status_code == 201
    assert response.json() == {'message': 'Set successfully'}
    assert client.put(f"/bulkcache", json=request_body2).status_code == status.HTTP_404_NOT_FOUND

def test_get_cache_values():
    key1, value1 = "key1", "value1"
    key2, value2 = "key2", "value2"
    key3, value3 = "key3", "value3"
    request_body = {"keys": [key1, key2, key3]}
    response = client.get("/bulkcache", params={"keys": ["key1", "key2", "key3"]})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"values": {key1: value1, key2: value2, key3: value3}}

def test_delete_bulk():
    response = client.delete("/bulkcache", params={"keys": ["key1", "key2", "key3"]})
    assert response.status_code == status.HTTP_204_NO_CONTENT
    
data1 = {
    "maxsize": 256,
    "ttl": 300
}
def test_configure_cache():
    response = client.put("/configure", json=data1)
    assert response.status_code == status.HTTP_202_ACCEPTED
    assert response.json() == {"data": f"new maxsize set to {data1['maxsize']} and ttl set to {data1['ttl']}"}


