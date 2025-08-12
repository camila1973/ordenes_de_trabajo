from typing import Optional

from pydantic import BaseModel, EmailStr

from app.api.v1.schemas.city_schema import CityResponse


class CompanyCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    phone: str
    address: str
    city_id: int
    class Config:
        from_attributes = True



class CompanyOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    phone: str
    address: str
    city:CityResponse
    class Config:
        from_attributes = True

class CompanyUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    phone: Optional[str]
    address: Optional[str]
    city_id: Optional[int]