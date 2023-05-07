from routers import singlecache, bulkcache, configurecache
from fastapi import FastAPI
from cacheout import Cache
from cacheout import Cache

cache = Cache(maxsize=256, ttl=0, default=None)

app = FastAPI()

app.include_router(singlecache.router)
app.include_router(bulkcache.router)
app.include_router(configurecache.router)

