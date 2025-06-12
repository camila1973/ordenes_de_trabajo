import logging
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.api.v1.models import GPS
from app.api.v1.schemas.gps_schema import GpsCreate
from sqlalchemy.exc import SQLAlchemyError


def create_GPS(db: Session, gps_data: GpsCreate):
    try:
        sim_existente = db.query(GPS).filter(GPS.sim_id == gps_data.sim_id).first()
        if sim_existente:
            raise HTTPException(
                status_code=400,
                detail="La SIM ya está asignada a otro GPS."
            )

        gps_new = GPS(
            GPSid=gps_data.GPSid,
            IMEI=gps_data.IMEI,
            brand_id=gps_data.brand_id,
            sim_id=gps_data.sim_id
        )
        db.add(gps_new)
        db.commit()
        db.refresh(gps_new)
        return gps_new

    except IntegrityError as e:
        db.rollback()
        if "unique constraint" in str(e.orig).lower():
            raise HTTPException(status_code=400, detail="El GPS ya existe.")
        raise HTTPException(status_code=500, detail="Error al crear GPS.")

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error en la base de datos: {str(e)}")

def get_gps(db: Session):
    try:
        return db.query(GPS).all()
    except Exception as e:
        logging.error(f"Error fetching GPSs: {e}")
        raise HTTPException(
            status_code=500,
            detail="Error al obtener GPSs."
        )