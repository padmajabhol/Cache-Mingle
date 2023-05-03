from typing import Union
from pydantic import BaseModel
from cacheout import Cache
from fastapi import HTTPException

from fastapi import FastAPI

app = FastAPI()

cache = Cache()

@app.put("/value/{key}")
def create_value(key: str, value: str):
    cache.set(key, value)
    return {"key": key, "value": value}

@app.get("/name/{key}")
def get_value(key: str):
    value = cache.get(key)
    if not value:
        raise HTTPException(status_code=404, detail=f"Value with key {key} not found")
    return {"key": key, "value": value}

@app.delete("/value/{key}")
def delete(key: str):
    cache.delete(key)
    return {'data': "value is deleted"}

@app.get("/values/keys")
def view_keys():
    keys = list(cache.keys())
    return {"keys": keys}
