import logging

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.api.v1.models.city import City
from app.api.v1.schemas.city_schema import CityCreate


def create_city(db: Session, city_data:CityCreate):
    city = City(name=city_data.name)
    db.add(city)
    try:
        db.commit()
        db.refresh(city)
        return city
    except IntegrityError as e:
        db.rollback()
        if "unique constraint" in str(e.orig).lower():
            raise HTTPException(status_code=400, detail="La ciudad ya existe.")
        raise HTTPException(status_code=500, detail="Error al crear ciudad.")

def get_cities(db: Session):
    try:
        return db.query(City).all()
    except Exception as e:
        logging.error(f"Error fetching cities: {e}")
        raise HTTPException(
            status_code=500,
            detail="Error al obtener las ciudades."
        )