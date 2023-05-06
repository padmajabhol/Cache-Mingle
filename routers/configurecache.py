from fastapi import APIRouter, status
from schema import Configure
from repository import configurecache

router = APIRouter(prefix="/configure", tags=["configure maxsize and ttl"])

@router.put("/",
            status_code=status.HTTP_202_ACCEPTED,
            summary="Configure cache",
            description="This API call updates the maxsize and time-to-live(expiry) of the cache.")
def configure(request: Configure):
    return configurecache.configure_cache(request)