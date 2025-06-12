import logging
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.api.v1.models.brandGps import Brand
from app.api.v1.schemas.branGps_schema import BrandGpsCreate

def create_brand(db: Session, brand_data:BrandGpsCreate):
    brand_new = Brand(name=brand_data.name)
    db.add(brand_new)
    try:
        db.commit()
        db.refresh(brand_new)
        return brand_new
    except IntegrityError as e:
        db.rollback()
        if "unique constraint" in str(e.orig).lower():
            raise HTTPException(status_code=400, detail="La marca ya existe.")
        raise HTTPException(status_code=500, detail="Error al crear la marca.")

def get_brands(db: Session):
    try:
        return db.query(Brand).all()
    except Exception as e:
        logging.error(f"Error fetching brands: {e}")
        raise HTTPException(
            status_code=500,
            detail="Error al obtener las marcas."
        )