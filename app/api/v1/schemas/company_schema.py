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