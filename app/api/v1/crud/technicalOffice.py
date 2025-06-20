import logging
from http.client import HTTPException

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.api.v1.models import TechnicalOffice, City
from app.api.v1.schemas.technicalOffice_schema import TechnicalOfficeCreate


def create_technical_office(db:Session,technicalOffice_data: TechnicalOfficeCreate):
    new_technicalOffice=TechnicalOffice(name=technicalOffice_data.name,
                                        city_id=technicalOffice_data.city_id)
    db.add(new_technicalOffice)
    try:
        db.commit()
        db.refresh(new_technicalOffice)
        return new_technicalOffice
    except IntegrityError as e:
        db.rollback()
        if "unique constraint" in str(e.orig).lower():
            raise HTTPException(status_code=400, detail="La oficina tecnica ya existe.")
        raise HTTPException(status_code=500, detail="Error al crear oficina tecnica.")

def get_technical_offices(db:Session):
    try:
        return db.query(TechnicalOffice).all()
    except Exception as e:
        logging.error(f"Error fetching SIMS: {e}")
        raise HTTPException(
            status_code=500,
            detail="Error al obtener las oficinas tecnicas."
        )

def update_technical_office(db: Session, office_id: int, update_data: dict):
    office = db.query(TechnicalOffice).filter(TechnicalOffice.id == office_id).first()

    if not office:
        raise HTTPException(status_code=404, detail="Technical office not found")

    if "city_id" in update_data:
        city = db.query(City).filter(City.id == update_data["city_id"]).first()
        if not city:
            raise HTTPException(status_code=400, detail="City not found")

    for key, value in update_data.items():
        setattr(office, key, value)

    db.commit()
    db.refresh(office)
    return office

def delete_technical_office(db: Session, technicalOffice_id: int):
    technicalOffice = db.query(TechnicalOffice).filter(TechnicalOffice.id == technicalOffice_id).first()

    if not technicalOffice:
        raise HTTPException(status_code=404, detail="technicalOffice not found")

    db.delete(technicalOffice)
    db.commit()
    return {"message": f"Owner with ID {technicalOffice_id} deleted successfully"}



