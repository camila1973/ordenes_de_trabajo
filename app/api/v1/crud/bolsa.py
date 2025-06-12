import logging
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.api.v1.models.bolsa import Bolsa
from app.api.v1.schemas.bolsa_schema import BolsaCreate
from datetime import date, timedelta



def create_bolsa(db: Session, bolsa_data:BolsaCreate):
    bolsa = Bolsa(name=bolsa_data.name,
                Megas=bolsa_data.Megas,
                cutting_day=bolsa_data.cutting_day)
    db.add(bolsa)
    try:
        db.commit()
        db.refresh(bolsa)
        return bolsa
    except IntegrityError as e:
        db.rollback()
        if "unique constraint" in str(e.orig).lower():
            raise HTTPException(status_code=400, detail="La bolsa ya existe.")
        raise HTTPException(status_code=500, detail="Error al crear la bolsa.")

def calcular_fecha_corte(cutting_day: int) -> date:
    today = date.today()
    if today.day > cutting_day:
        if today.month == 12:
            return date(today.year + 1, 1, cutting_day)
        return date(today.year, today.month + 1, cutting_day)
    else:
        return date(today.year, today.month, cutting_day)


def get_bolsas(db: Session):
    try:
        return db.query(Bolsa).all()
    except Exception as e:
        logging.error(f"Error fetching bolsas: {e}")
        raise HTTPException(
            status_code=500,
            detail="Error al obtener las bolsas."
        )