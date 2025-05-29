from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    phone: str
    username: str
    password: str
    role_id: int

    class Config:
        from_attributes = True

class UserResponse(BaseModel):
    id: int
    name: str
    last_name: str
    email: str
    phone: str
    username: str
    role_id: int

    class Config:
        from_attributes = True