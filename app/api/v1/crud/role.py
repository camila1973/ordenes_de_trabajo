import logging

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.api.v1.models.role import Role
from app.api.v1.schemas.role_schema import RoleCreate


def create_role(db: Session, role_data:RoleCreate):
    role= Role(name=role_data.name)
    db.add(role)
    try:
        db.commit()
        db.refresh(role)
        return role
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="El rol ya existe.")


def get_roles(db: Session):
    try:
        return db.query(Role).all()
    except Exception as e:
        logging.error(f"Error fetching roles: {e}")
        raise HTTPException(
            status_code=500,
            detail="Error al obtener los roles."
        )