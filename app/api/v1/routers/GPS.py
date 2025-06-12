from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.v1.crud.brandGps import create_brand, get_brands
from app.api.v1.crud.gps import create_GPS, get_gps
from app.api.v1.schemas.branGps_schema import BrandGpsOut, BrandGpsCreate
from app.api.v1.schemas.gps_schema import GpsOut, GpsCreate, GpsResponse
from app.api.v1.utils.db import get_db


router = APIRouter(prefix="/gps", tags=["GPSs"])

@router.post("/brand", response_model=BrandGpsOut)
def crear_marcaGps(brand: BrandGpsCreate, db: Session = Depends(get_db)):
    return create_brand(db, brand)

@router.get("/brands", response_model=list[BrandGpsOut])
def listar_marcasGps(db: Session = Depends(get_db)):
    return get_brands(db)

@router.post("/", response_model=GpsResponse)
def crear_GPS(gps: GpsCreate, db: Session = Depends(get_db)):
    return create_GPS(db, gps)

@router.get("/", response_model=list[GpsOut])
def listar_GPSs(db: Session = Depends(get_db)):
    return get_gps(db)

