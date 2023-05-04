from typing import Union
from pydantic import BaseModel
from cacheout import Cache
from fastapi import HTTPException

from fastapi import FastAPI

app = FastAPI()

cache = Cache(maxsize=256, ttl=0, default=None)

class Value(BaseModel):
    key: str
    value: str
    
@app.put("/value/{key}")
def create_value(request: Value):
    key_value = request.key
    value_value = request.value
    cache.set(key_value, value_value)
    return {"key": key_value, "value": value_value}

@app.get("/value/{key}")
def get_value(key: str):
    value = cache.get(key)
    if not value:
        raise HTTPException(status_code=404, detail=f"Value with key {key} not found")
    return {"key": key, "value": value}

@app.get("/values/keys")
def view_keys():
    keys = list(cache.keys())
    return {"keys": keys}

@app.delete("/value/{key}")
def delete(key: str):
    cache.delete(key)
    return {'data': "value is deleted"}

@app.get("/value")
def get_entire_cache():
    value = cache.copy()
    return {"value": value}

