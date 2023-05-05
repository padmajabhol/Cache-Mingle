from pydantic import BaseModel
from typing import List 

class Value(BaseModel):
    key: str
    value: str


class BulkValue(BaseModel):
    key: str
    value: str

class CreateBulkValue(BaseModel):
    items: List[BulkValue]


class Configure(BaseModel):
    maxsize: int
    ttl: int