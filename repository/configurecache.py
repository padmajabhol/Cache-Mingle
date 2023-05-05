import main
from schema import Configure

def configure_cache(request: Configure):
    maxsize_value = request.maxsize
    ttl_values = request.ttl
    main.cache.configure(maxsize=maxsize_value, ttl=ttl_values)
    return {'data': f"new maxsize set to {maxsize_value} and ttl set to {ttl_values}"}