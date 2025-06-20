from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.v1.crud.city import get_cities, create_city, update_city, delete_city
from app.api.v1.schemas.city_schema import CityResponse, CityCreate, CityUpdateDto
from app.api.v1.utils.db import get_db

router = APIRouter(prefix="/cities", tags=["Cities"])

@router.get("/",response_model=list[CityResponse])
def list_cities(db: Session = Depends(get_db)):
    return get_cities(db)

@router.post('/', response_model=CityResponse)
def crear_ciudad(city: CityCreate, db: Session = Depends(get_db)):
    return create_city(db, city)

@router.put('/{id}', response_model=CityUpdateDto)
def update_city_endpoint(id:int,data:CityUpdateDto,db:Session=Depends(get_db)):
    return update_city(db,id,data.dict(exclude_unset=True))
@router.delete('/{city_id}')
def delete_city_endpoint(city_id: int, db: Session = Depends(get_db)):
    return delete_city(city_id,db)
