from fastapi import APIRouter
from schema import Configure
from repository import configurecache

router = APIRouter()

@router.put("/configure")
def configure(request: Configure):
    return configurecache.configure_cache(request)