import logging

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.api.v1.models import Owner, Company
from app.api.v1.schemas.owner_schema import OwnerCreateDto


def create_owner(db: Session, owner_data: OwnerCreateDto):
    # Buscar las empresas si se especifican
    companies = []
    if owner_data.company_ids:
        companies = db.query(Company).filter(Company.id.in_(owner_data.company_ids)).all()

    new_owner = Owner(
        name=owner_data.name,
        last_name=owner_data.last_name,
        document_id=owner_data.document_id,
        phone=owner_data.phone,
        email=owner_data.email,
        companies=companies  # 👈 asignación
    )

    db.add(new_owner)
    db.commit()
    db.refresh(new_owner)
    return new_owner

def update_owner(
    db: Session,
    owner_id: int,
    updated_data: dict,
    new_company_ids: list[int] = None
):
    owner = db.query(Owner).filter(Owner.id == owner_id).first()
    if not owner:
        raise HTTPException(status_code=404, detail="Owner not found")

    for key, value in updated_data.items():
        setattr(owner, key, value)

    # Reemplazar empresas asociadas (si se envían)
    if new_company_ids is not None:
        companies = db.query(Company).filter(Company.id.in_(new_company_ids)).all()
        owner.companies = companies

    db.commit()
    db.refresh(owner)
    return owner

def get_owners(db: Session):
    try:
        return db.query(Owner).all()
    except Exception as e:
        logging.error(f"Error fetching cities: {e}")
        raise HTTPException(
            status_code=500,
            detail="Error al obtener los propietarios."
        )

def delete_owner(db: Session, owner_id: int):
    owner = db.query(Owner).filter(Owner.id == owner_id).first()

    if not owner:
        raise HTTPException(status_code=404, detail="Owner not found")

    db.delete(owner)
    db.commit()
    return {"message": f"Owner with ID {owner_id} deleted successfully"}