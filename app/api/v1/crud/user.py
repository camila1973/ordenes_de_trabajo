import logging
from datetime import timedelta, datetime

from jose import jwt
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.api.v1.models.user import User
from app.api.v1.schemas.user_schema import UserCreate
from passlib.context import CryptContext
from app.api.v1.utils.settings import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)

    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)

def create_user( db: Session, user_data: UserCreate):
    try:
        db_user= User(
            name=user_data.name,
            last_name=user_data.last_name,
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
    except Exception as e:
        db.rollback()
        print(f"Error inesperado: {e.__class__.__name__}: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")


def get_users(db: Session):
    try:
        return db.query(User).all()
    except Exception as e:
        logging.error(f"Error fetching users: {e}")
        raise HTTPException(
            status_code=500,
            detail="Error al obtener los usuarios."
        )