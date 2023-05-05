from typing import List
from fastapi import APIRouter, Query
from schema import CreateBulkValue
from repository import bulkcache

router = APIRouter()

@router.put("/bulkcache")
def create(request: CreateBulkValue):
    return bulkcache.set_bulk_value(request)

@router.get("/bulkcache")
def get(keys: List[str] = Query(None)):
    return bulkcache.get_cache_values(keys)

@router.delete("/bulkcache")
def delete(keys: List[str] = Query(None)):
    return bulkcache.delete_bulk(keys)
    