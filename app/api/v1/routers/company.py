from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.v1.crud.company import create_company, get_companies
from app.api.v1.schemas.company_schema import CompanyOut, CompanyCreate
from app.api.v1.utils.db import get_db

router = APIRouter(prefix="/companies", tags=["Companies"])

@router.post("/", response_model=CompanyOut)
def crear_empresa(company: CompanyCreate, db: Session = Depends(get_db)):
    return create_company(db, company)

@router.get("/", response_model=list[CompanyOut])
def listar_empresas(db: Session = Depends(get_db)):
    return get_companies(db)

