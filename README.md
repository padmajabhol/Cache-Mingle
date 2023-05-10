# Cache-Mingle
A microservice built using FastAPI and cacheout that can store and retrive data from an in-memory cache for internal use.

## Technology Stack
- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Cacheout](https://cacheout.readthedocs.io/en/latest/#)
- [Render](https://render.com/)

## Installation

Before setting up the project make sure the python version is >= 3.7.

1. Fork the [Cache-mingle repository](https://github.com/padmajabhol/Cache-Mingle).
2. Clone the repository:
  ```sh
  git clone git@github.com:<USERNAME>/Cache-Mingle.git && cd Cache-Mingle
  ```
  Replace the `<USERNAME>` with your GitHub username.

3. Setup and activate Virtual Environment:
``` bash
$ virtualenv env
$ source env/bin/activate
```
4. Install dependencies
```bash
$ pip install -r requirements.txt
```
5. Restart the terminal and run project
```bash
uvicorn main:app --reload
```

You can also run unit tests and code coverage using the commands:

Unit Tests:

``` bash
$ pytest
```

Code coverage: 

```bash
$ pytest --cov
```

After running tests with code coverage, you can get the report:
```bash

---------- coverage: platform darwin, python 3.11.2-final-0 ----------
Name                           Stmts   Miss  Cover
--------------------------------------------------
main.py                            9      0   100%
repository/bulkcache.py           21      0   100%
repository/configurecache.py       7      0   100%
repository/singlecache.py         26      1    96%
routers/bulkcache.py              14      0   100%
routers/configurecache.py          7      0   100%
routers/singlecache.py            19      0   100%
schema.py                         17      0   100%
test_main.py                      58      0   100%
--------------------------------------------------
TOTAL                            178      1    99%
```

## Endpoints

| Endpoint       |  Functionality            |
| :--------------| :------------------------ |
| **GET /cache/{key}**  | This API call simulates fetching a single value corresponding to its key. Key is a mandatory path vbariable. |
| **PUT /cache/{key}**  | This API call creates a value corresponding to a key. Key and Value are mandatory. |
| **DELETE /cache/{key}** | This API call deletes a key and its respected value. Key is a mandatory path variable. |
| **GET /cache/all/keys**  | This API call simulates fetching all keys. |
| **GET /cache**  | This API call simulates fetching all keys and their respected values. |
| **GET /bulkcache**  | This API call simulates fetching bulk values and their keys. |
| **PUT /bulkcache**  | This API call creates a bulk values corresponding to their keys. Key and Value are mandatory. |
| **DELETE /bulkcache**  | This API call bulk deletes values and their keys. |
| **PUT /configure** | This API call updates the maxsize and time-to-live(expiry) of the cache. |

## Request Bodies

### Configure cache
<code>
PUT /configure/
</code>

```json
{
  "maxsize": "Maximum cache size",
  "ttl": "TTL (time-to-live)"
}
```
The type for the above properties would be:-

* **maxsize** : *int* (Optional)
* **ttl** : *int* (Optional)

### Create single data
<code>
PUT /cache/{key}
</code>

```json
{
  "key": "key of the value",
  "value": "the value that goes in"
}
```
The type for the above properties would be:-

* **key** : *str* 
*  **value** : *str*

### Create bulk data
<code>
PUT /bulkcache/
</code>

```json
{
  "items": [
    {
      "key": "key of the value",
      "value": "the value that goes in"
    }
  ]
}
```
The type for the above properties would be:-
* **key** : *str* 
*  **value** : *str*
  




