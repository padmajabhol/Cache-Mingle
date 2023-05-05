from typing import Union, List , Dict
from pydantic import BaseModel
from cacheout import Cache
from fastapi import HTTPException, Query
from routers import singlecache

from fastapi import FastAPI

app = FastAPI()

cache = Cache(maxsize=256, ttl=0, default=None)

app.include_router(singlecache.router)

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
    



