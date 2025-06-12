from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.api.v1.utils.db import Base


class Firmware(Base):
    __tablename__ = 'firmware'
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String, unique=True, index=True)
    description = Column(String)
    archivo1 = Column(String, nullable=True)  # No obligatorio
    archivo2 = Column(String, nullable=True)  # No obligatorio

    equipments=relationship("Equipment", back_populates="firmware_equipment")

