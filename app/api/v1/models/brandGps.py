from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.api.v1.utils.db import Base

class Brand(Base):
    __tablename__ = 'brands'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    gps_devices=relationship("GPS", back_populates="brand")
