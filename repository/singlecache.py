from schema import Value
import main
from fastapi import HTTPException

def create_cache(request: Value):
    key_value = request.key
    value_value = request.value
    main.cache.set(key_value, value_value)
    return {"key": key_value, "value": value_value}

def get_cache(key: str):
    value = main.cache.get(key)
    if not value:
        raise HTTPException(status_code=404, detail=f"Value with key {key} not found")
    return {"key": key, "value": value}

def view_keys():
    keys = list(main.cache.keys())
    return {"keys": keys}

def delete_cache(key: str):
    main.cache.delete(key)
    return {'data': "value is deleted"}

def get_entire_cache():
    value = main.cache.copy()
    return {"value": value}