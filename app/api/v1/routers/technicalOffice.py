from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.api.v1.crud.technicalOffice import get_technical_offices, create_technical_office, update_technical_office, \
    delete_technical_office
from app.api.v1.schemas.technicalOffice_schema import TechnicalOfficeCreate, TechnicalOfficeOut, \
    TechnicalOfficeUpdateDto
from app.api.v1.utils.db import get_db

router = APIRouter(prefix="/technical-offices", tags=["Technical Offices"])

@router.get("/",response_model=list[TechnicalOfficeOut])
def get_technical_office_endpoint(db:Session= Depends(get_db)):
    return get_technical_offices(db)

@router.post("/", response_model=TechnicalOfficeCreate)
def create_technical_office_endpoint(technical_office:TechnicalOfficeCreate, db:Session= Depends(get_db)):
    return create_technical_office(db, technical_office)

@router.put("/{technical_office_id}", response_model=TechnicalOfficeUpdateDto)
def update_technical_office_endpoint(technical_office_id:int,data:TechnicalOfficeUpdateDto,db:Session=Depends(get_db)):
    return update_technical_office(db,technical_office_id,data.dict(exclude_unset=True))

@router.delete("/{technical_office_id}")
def delete_technical_office_endpoint(technical_office_id:int,db:Session=Depends(get_db)):
    return delete_technical_office(db,technical_office_id)