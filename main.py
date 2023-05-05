from typing import Union, List , Dict
from pydantic import BaseModel
from cacheout import Cache
from fastapi import HTTPException, Query

from fastapi import FastAPI

app = FastAPI()

cache = Cache(maxsize=256, ttl=0, default=None)

class Value(BaseModel):
    key: str
    value: str
    
@app.put("/cache/{key}")
def create_value(request: Value):
    key_value = request.key
    value_value = request.value
    cache.set(key_value, value_value)
    return {"key": key_value, "value": value_value}

@app.get("/cache/{key}")
def get_value(key: str):
    value = cache.get(key)
    if not value:
        raise HTTPException(status_code=404, detail=f"Value with key {key} not found")
    return {"key": key, "value": value}

@app.get("/caches/keys")
def view_keys():
    keys = list(cache.keys())
    return {"keys": keys}

@app.delete("/cache/{key}")
def delete(key: str):
    cache.delete(key)
    return {'data': "value is deleted"}

@app.get("/cache")
def get_entire_cache():
    value = cache.copy()
    return {"value": value}



class BulkValue(BaseModel):
    key: str
    value: str

class CreateBulkValue(BaseModel):
    items: List[BulkValue]

@app.put("/bulkcache")
def set_bulk_value(request: CreateBulkValue):
    for item in request.items:
        key = item.key
        value = item.value
        cache.set(key, value )
    return {"message": "Set successfully"}


@app.get("/bulkcache")
def get_cache_values(keys: List[str] = Query(None)):
    values = cache.get_many(keys)
    return {"values": values}


class DeleteBulkValue(BaseModel):
    keys: List[str]

@app.delete("/bulkcache")
def delete_bulk(keys: List[str] = Query(None)):
    keys1 = []
    for key in keys:
        keys1.append(key)
        cache.delete_many(keys1)
    return {'data': 'values are deleted'}



class Configure(BaseModel):
    maxsize: int
    ttl: int

@app.put("/configure")
def configure_cache(request: Configure):
    maxsize_value = request.maxsize
    ttl_values = request.ttl
    cache.configure(maxsize=maxsize_value, ttl=ttl_values)
    return {'data': f"new maxsize set to {maxsize_value} and ttl set to {ttl_values}"}
    



