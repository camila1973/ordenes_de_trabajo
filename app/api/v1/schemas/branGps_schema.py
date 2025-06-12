from pydantic import BaseModel


class BrandGpsCreate(BaseModel):
    name:str
    class Config:
        from_attributes = True

class BrandGpsOut(BaseModel):
    id:int
    name:str
    class Config:
        from_attributes = True