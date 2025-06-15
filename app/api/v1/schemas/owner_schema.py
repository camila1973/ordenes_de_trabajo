from typing import Optional, List
from pydantic import BaseModel, EmailStr


class OwnerUpdateDto(BaseModel):
    name: str
    last_name: str
    document_id: str
    phone: str
    email: str
    company_ids: Optional[List[int]] = None

    class Config:
            from_attributes = True


class OwnerCreateDto(BaseModel):
    name: str
    last_name: str
    document_id: str
    phone: str
    email: EmailStr
    company_ids: Optional[List[int]] = None  # empresas asociadas (opcional)

    class Config:
        from_attributes = True

class OwnerReadDto(BaseModel):
    id: int
    name: str
    last_name: str
    document_id: str
    phone: str
    email: str

    class Config:
        from_attributes = True
