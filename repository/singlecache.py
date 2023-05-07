from schema import Value
import main
from fastapi import HTTPException,status

def create_cache(request: Value):
    key_value = request.key.strip()
    value_value = request.value
    if not key_value:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid key")
    main.cache.set(key_value, value_value)
    return {"key": key_value, "value": value_value}

def get_cache(key: str):
    value = main.cache.get(key)
    if not value:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Value with key {key} not found")
    return {"key": key, "value": value}

def view_keys():
    keys = list(main.cache.keys())
    return {"keys": keys}

def delete_cache(key: str):
    main.cache.delete(key)
    if not key:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {"data": "value is deleted"}

def get_entire_cache():
    values = main.cache.copy()
    return {"data": values}