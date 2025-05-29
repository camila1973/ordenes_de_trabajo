from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.api.v1.models.user import User
from app.api.v1.schemas.user_schema import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user( db: Session, user_data: UserCreate):
    try:
        db_user= User(
            name=user_data.name,
            last_name=user_data.LastName,
            email=user_data.email,
            phone=user_data.phone,
            username=user_data.username,
            password_hash = pwd_context.hash(user_data.password),
            role_id=user_data.role_id
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError as e:
        db.rollback()
        error_msg = str(e).lower()
        if "email" in error_msg:
            raise HTTPException(400, "El email ya está registrado")
        elif "username" in error_msg:
            raise HTTPException(400, "El username ya existe")
        elif "phone" in error_msg:
            raise HTTPException(status_code=400, detail="El teléfono ya existe")
        else:
            raise HTTPException(status_code=400, detail="Error de datos duplicados")



