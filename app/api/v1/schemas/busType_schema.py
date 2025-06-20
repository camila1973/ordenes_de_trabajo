from typing import Optional

from pydantic import BaseModel


class BusTypeCreate(BaseModel):
    name:str
    class Config:
        from_attributes = True

class BusTypeOut(BaseModel):
    id:int
    name:str
    class Config:
        from_attributes = True

class BusTypeUpdate(BaseModel):
    name: Optional[str] = None