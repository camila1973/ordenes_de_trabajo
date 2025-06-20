from typing import Optional

from pydantic import BaseModel, constr


class CityCreate(BaseModel):
    name: constr(min_length=3, max_length=50)

class CityResponse(BaseModel):
    id: int
    name: str
    class Config:
        from_attributes = True

class CityUpdateDto(BaseModel):
    name: Optional[str] = None