from pydantic import BaseModel, validator
from typing import List, Optional

class Value(BaseModel):
    key: str
    @validator("key", pre=True, always=True)
    def check_ids(cls, key):
        assert len(key) > 0, "ID's cannot be empty."
        return key
    value: str


class BulkValue(BaseModel):
    key: str
    value: str

class CreateBulkValue(BaseModel):
    items: List[BulkValue]


class Configure(BaseModel):
    maxsize: Optional[int] = None
    ttl: Optional[int] = None