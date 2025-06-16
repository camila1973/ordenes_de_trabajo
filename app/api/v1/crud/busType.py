import logging

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.api.v1.models import BusType
from app.api.v1.schemas.busType_schema import BusTypeCreate


def create_bus_type(db:Session, bus_type:BusTypeCreate):
    new_bus_type = BusType(name=bus_type.name)
    db.add(new_bus_type)
    try:
        db.commit()
        db.refresh(new_bus_type)
        return new_bus_type
    except IntegrityError as e:
        db.rollback()
        if "unique constraint" in str(e.orig).lower():
            raise HTTPException(status_code=400, detail="La ciudad ya existe.")
        raise HTTPException(status_code=500, detail="Error al crear ciudad.")


def get_bus_types(db:Session):
    try:
        return db.query(BusType).all()
    except Exception as e:
        logging.error(f"Error fetching cities: {e}")
        raise HTTPException(
            status_code=500,
            detail="Error al obtener las ciudades."
        )

def update_bus_type(db:Session, bus_type_id:int, bus_type:dict):
    bus_type_db = db.query(BusType).filter(BusType.id == bus_type_id).first()
    if not bus_type_db:
        raise HTTPException(status_code=404, detail="El tipo de bus no existe.")

    for key,value in bus_type.items():
        setattr(bus_type_db, key, value)

    db.commit()
    db.refresh(bus_type_db)
    return bus_type_db

def delete_bus_type(db: Session, bus_type_id:int):
    bus_type_db = db.query(BusType).filter(BusType.id == bus_type_id).first()
    if not bus_type_db:
        raise HTTPException(status_code=404, detail="El tipo de bus no existe.")

    db.delete(bus_type_db)