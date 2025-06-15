from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.api.v1.models.company_owner import company_owner
from app.api.v1.utils.db import Base


class Owner(Base):
    __tablename__ = 'owners'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    last_name = Column(String, index=True)
    document_id = Column(String, unique=True, nullable=False)
    phone= Column(String, index=True)
    email = Column(String, index=True)

    companies= relationship("Company", secondary=company_owner, back_populates="owners")
