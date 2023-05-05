from pydantic import BaseModel

class Value(BaseModel):
    key: str
    value: str
