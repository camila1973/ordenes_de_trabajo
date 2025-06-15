from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.api.v1.utils.db import Base

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    companies = relationship("Company", back_populates="city")
    technical_offices = relationship("TechnicalOffice", back_populates="city")