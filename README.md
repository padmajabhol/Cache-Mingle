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
5. Run project
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



