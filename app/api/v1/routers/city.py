from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.v1.crud.city import get_cities, create_city
from app.api.v1.schemas.city_schema import CityResponse, CityCreate
from app.api.v1.utils.db import get_db

router = APIRouter(prefix="/cities", tags=["Cities"])

@router.get("/",response_model=list[CityResponse])
def list_cities(db: Session = Depends(get_db)):
    return get_cities(db)

@router.post('/', response_model=CityResponse)
def crear_ciudad(city: CityCreate, db: Session = Depends(get_db)):
    return create_city(db, city)
