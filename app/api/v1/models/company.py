from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.api.v1.utils.db import Base


class Company(Base):
    __tablename__ = 'companies'
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String, unique=True, index=True)
    email=Column(String, unique=True, index=True)
    phone=Column(String, index=True)
    address=Column(String, index=True)

    city_id=Column(Integer, ForeignKey('cities.id'))
    city= relationship("City", back_populates="companies")