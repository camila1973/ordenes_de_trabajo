from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.v1.utils.db import get_db
from app.api.v1.schemas.role_schema import RoleCreate, RoleOut
from app.api.v1.crud.role import create_role, get_roles

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.post("/", response_model=RoleOut)
def crear_rol(role: RoleCreate, db: Session = Depends(get_db)):
    return create_role(db, role)

@router.get("/", response_model=list[RoleOut])
def listar_roles(db: Session = Depends(get_db)):
    return get_roles(db)
print("📦 Cargando router de roles")
