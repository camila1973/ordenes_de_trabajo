from datetime import date
from pydantic import BaseModel

class BolsaCreate(BaseModel):
    name:str
    Megas:int
    cutting_day: int

    class Config:
        from_attributes = True

class BolsaOut(BaseModel):
    id: int
    name: str
    Megas: int
    cutting_day: int
    cutting_date: date

    class Config:
        orm_mode = True


class BolsaResponse(BaseModel):
    id: int
    name: str
    Megas: int
    cutting_day: int

    class Config:
        orm_mode = True