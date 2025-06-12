from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.api.v1.crud.bolsa import get_bolsas, create_bolsa
from app.api.v1.schemas.bolsa_schema import BolsaOut, BolsaResponse, BolsaCreate
from app.api.v1.utils.db import get_db

router = APIRouter(prefix="/bolsas", tags=["Bolsas"])

@router.get("/",response_model=list[BolsaOut])
def list_bolsas(db: Session = Depends(get_db)):
    return get_bolsas(db)

@router.post('/', response_model=BolsaResponse)
def crear_bolsa(bolsa: BolsaCreate, db: Session = Depends(get_db)):
    return create_bolsa(db, bolsa)