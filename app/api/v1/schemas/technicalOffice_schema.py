from pydantic import BaseModel

from app.api.v1.schemas.city_schema import CityResponse
from typing import Optional


class TechnicalOfficeCreate(BaseModel):
    name: str
    city_id: int
    class Config:
        from_attributes = True

class TechnicalOfficeOut(BaseModel):
    id: int
    name: str
    city_id:CityResponse
    class Config:
        from_attributes = True



class TechnicalOfficeUpdateDto(BaseModel):
    name: Optional[str] = None
    city_id: Optional[int] = None