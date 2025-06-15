from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.v1.crud.owner import create_owner, update_owner, get_owners, delete_owner
from app.api.v1.schemas.owner_schema import OwnerCreateDto, OwnerUpdateDto, OwnerReadDto
from app.api.v1.utils.db import get_db

router = APIRouter(prefix="/owners", tags=["Owners"])

@router.post("/", status_code=201, response_model=OwnerCreateDto)
def create_owner_endpoint(owner: OwnerCreateDto, db: Session = Depends(get_db)):
    return create_owner(db=db, owner_data=owner)


@router.put("/{owner_id}", response_model=OwnerUpdateDto)
def edit_owner(owner_id: int, data: OwnerUpdateDto, db: Session = Depends(get_db)):
    updated_data = {
        "name": data.name,
        "last_name": data.last_name,
        "document_id": data.document_id,
        "phone": data.phone,
        "email": data.email
    }
    return update_owner(
        db=db,
        owner_id=owner_id,
        updated_data=updated_data,
        new_company_ids=data.company_ids  # esto puede ser None si no se quiere editar
    )

@router.get("/", response_model=list[OwnerReadDto])
def get_owner_endpoint(db: Session = Depends(get_db)):
    return get_owners(db)


@router.delete("/{owner_id}")
def delete_owner_endpoint(owner_id: int, db: Session = Depends(get_db)):
    return delete_owner(db, owner_id)
