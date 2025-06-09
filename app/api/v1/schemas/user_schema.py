from pydantic import BaseModel, EmailStr

from app.api.v1.schemas.role_schema import RoleOut


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
    role: RoleOut

    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
      access_token: str
      token_type: str = "bearer"
      user_id: int
      email: str
      role: str
