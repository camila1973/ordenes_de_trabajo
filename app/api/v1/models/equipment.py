from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import foreign, relationship

from app.api.v1.utils.db import Base


class Equipment(Base):
    __tablename__ = 'equipment'
    id=Column(Integer, primary_key=True)
    serial_tarjeta=Column(String)

    firmware_id=Column(Integer, ForeignKey("firmware.id"))
    gps_id=Column(Integer, ForeignKey("gps.id"),unique=True)

    firmware_equipment=relationship("Firmware", back_populates="equipments")
    gps_equipment=relationship("GPS", back_populates="equipment",uselist=False)

