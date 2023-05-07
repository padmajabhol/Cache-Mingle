from typing import List
from fastapi import APIRouter, Query, status
from schema import CreateBulkValue
from repository import bulkcache

router = APIRouter(prefix="/bulkcache", tags=['bulk cache'])

@router.put("/", 
            status_code=status.HTTP_201_CREATED,
            summary="Create bulk data",
            description="This API call creates a bulk values corresponding to their keys. **Key** and **Value** are mandatory.")
def create(request: CreateBulkValue):
    return bulkcache.set_bulk_value(request)

@router.get("/", 
            status_code=status.HTTP_200_OK,
            summary="Retrieve bulk data",
            description="This API call simulates fetching bulk values and their keys.")
def get(keys: List[str] = Query(None)):
    return bulkcache.get_cache_values(keys)

@router.delete("/",
               status_code=status.HTTP_204_NO_CONTENT,
               summary="Delete bulk data",
               description="This API call bulk deletes values and their keys.")
def delete(keys: List[str] = Query(None)):
    return bulkcache.delete_bulk(keys)
    