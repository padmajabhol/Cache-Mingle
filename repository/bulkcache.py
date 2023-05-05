from schema import CreateBulkValue
from typing import List
from fastapi import Query
import main

def set_bulk_value(request: CreateBulkValue):
    for item in request.items:
        key = item.key
        value = item.value
        main.cache.set(key, value )
    return {"message": "Set successfully"}

def get_cache_values(keys: List[str] = Query(None)):
    values = main.cache.get_many(keys)
    return {"values": values}

def delete_bulk(keys: List[str] = Query(None)):
    keys1 = []
    for key in keys:
        keys1.append(key)
        main.cache.delete_many(keys1)
    return {'data': 'values are deleted'}