from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.v1.crud.busType import get_bus_types, create_bus_type, update_bus_type, delete_bus_type
from app.api.v1.schemas.busType_schema import BusTypeOut, BusTypeCreate, BusTypeUpdate
from app.api.v1.utils.db import get_db

router=APIRouter(prefix="/bus_type", tags=["bus_type"])

@router.get("/",response_model=list[BusTypeOut])
def get_bus_types_endpoint(db:Session=Depends(get_db)):
    return get_bus_types(db)


@router.post("/",response_model=BusTypeCreate)
def create_bus_type_endpoint(bus_type:BusTypeCreate,db:Session=Depends(get_db)):
    return create_bus_type(db, bus_type)

@router.put("/{id}",response_model=BusTypeOut)
def update_bus_type_endpoint( busType_id:int, bus_type:BusTypeUpdate,db:Session=Depends(get_db)):
    return update_bus_type(db, busType_id, bus_type.dict(exclude_unset=True))

@router.delete("/{id}")
def delete_bus_type_endpoint(busType_id:int,db:Session=Depends(get_db)):
    return delete_bus_type(db, busType_id)


