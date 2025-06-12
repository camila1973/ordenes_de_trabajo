import logging
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.api.v1.models.SIM import SIM
from app.api.v1.schemas.sim_schema import SimCreate


def create_sim(db: Session, sim_data:SimCreate):
    sim = SIM(  IMEI_sim=sim_data.IMEI_sim,
                phone=sim_data.phone,
                bolsa_id=sim_data.bolsa_id)
    db.add(sim)
    try:
        db.commit()
        db.refresh(sim)
        return sim
    except IntegrityError as e:
        db.rollback()
        if "unique constraint" in str(e.orig).lower():
            raise HTTPException(status_code=400, detail="La sim ya existe.")
        raise HTTPException(status_code=500, detail="Error al crear sim.")

def get_sims(db: Session):
    try:
        return db.query(SIM).all()
    except Exception as e:
        logging.error(f"Error fetching SIMS: {e}")
        raise HTTPException(
            status_code=500,
            detail="Error al obtener las SIMs."
        )