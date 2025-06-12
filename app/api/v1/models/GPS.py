from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.api.v1.utils.db import Base


class GPS(Base):
    __tablename__ = 'gps'
    id=Column(Integer, primary_key=True, index=True)
    GPSid=Column(String, index=True)
    IMEI=Column(String, index=True)

    brand_id=Column(Integer, ForeignKey("brands.id"))
    brand=relationship("Brand", back_populates="gps_devices")

    sim_id=Column(Integer, ForeignKey("sim.id"))
    SIM=relationship("SIM", back_populates="gps_device", uselist=False)

    equipment=relationship("Equipment", back_populates="gps_equipment",uselist=False)
