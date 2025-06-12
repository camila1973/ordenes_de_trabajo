import logging
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.api.v1.models import Company
from app.api.v1.schemas.company_schema import CompanyCreate


def create_company(db: Session, company_data:CompanyCreate):
    company= Company( name=company_data.name,
                   email=company_data.email,
                   phone=company_data.phone,
                   address=company_data.address,
                   city_id=company_data.city_id
                )
    db.add(company)
    try:
        db.commit()
        db.refresh(company)
        return company
    except IntegrityError as e:
        db.rollback()
        if "unique constraint" in str(e.orig).lower():
            raise HTTPException(status_code=400, detail="La empresa ya existe.")
        raise HTTPException(status_code=500, detail="Error al crear empresa.")

def get_companies(db: Session):
    try:
        return db.query(Company).all()
    except Exception as e:
        logging.error(f"Error fetching empresas: {e}")
        raise HTTPException(
            status_code=500,
            detail="Error al obtener las empresas."
        )