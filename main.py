import uvicorn
from routers import singlecache, bulkcache, configurecache
from cacheout import Cache
from fastapi import FastAPI

app = FastAPI()

cache = Cache(maxsize=256, ttl=0, default=None)

app.include_router(singlecache.router)
app.include_router(bulkcache.router)
app.include_router(configurecache.router)

