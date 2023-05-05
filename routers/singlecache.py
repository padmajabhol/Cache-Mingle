from pydantic import BaseModel
from fastapi import APIRouter
from cacheout import Cache
from schema import Value
from repository import singlecache
import main

router = APIRouter()
    
@router.put("/cache/{key}")
def create(request: Value):
    return singlecache.create_cache(request)

@router.get("/cache/{key}")
def get(key: str):
    return singlecache.get_cache(key)

@router.get("/caches/keys")
def view_all_keys():
    return singlecache.view_keys()

@router.delete("/cache/{key}")
def delete(key: str):
    return singlecache.delete_cache(key)

@router.get("/cache")
def get_all():
    return singlecache.get_entire_cache()
