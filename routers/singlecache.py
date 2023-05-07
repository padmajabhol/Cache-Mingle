from fastapi import APIRouter, status
from schema import Value
from repository import singlecache

router = APIRouter(prefix="/cache", tags=['operations'])
    
@router.put("/{key}",
            status_code=status.HTTP_201_CREATED,
            summary="Create data", 
            description="This API call creates a value corresponding to a key. **Key** and **Value** are mandatory.")
def create(request: Value):
    return singlecache.create_cache(request)

@router.get("/{key}", 
            status_code=status.HTTP_200_OK, 
            summary="Retrieve data",
            description="This API call simulates fetching a single value corresponding to its key. **Key** is a mandatory path vbariable.")
def get(key: str):
    return singlecache.get_cache(key)

@router.get("/all/keys", 
            status_code=status.HTTP_200_OK,
            summary="Retrieve all keys",
            description="This API call simulates fetching all keys.")
def view_all_keys():
    return singlecache.view_keys()

@router.delete("/{key}",
               status_code=status.HTTP_204_NO_CONTENT,
               summary="Delete data",
               description="This API call deletes a key and its respected value. **Key** is a mandatory path variable.")
def delete(key: str):
    return singlecache.delete_cache(key)

@router.get("/", 
            status_code=status.HTTP_200_OK,
            summary="Get all data",
            description="This API call simulates fetching all keys and their respected values.")
def get_all():
    return singlecache.get_entire_cache()
