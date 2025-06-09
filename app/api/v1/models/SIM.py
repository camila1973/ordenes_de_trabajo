from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.api.v1.utils.db import Base


class SIM(Base):
    __tablename__='sims'
    id=Column(Integer,primary_key=True)
    IMEI_sim=Column(String, index=True)
    phone=Column(String,index=True)

    bolsa_id=Column(Integer,ForeignKey('bolsa.id'))
    bolsa=relationship("Bolsa",back_populates="SIM")


