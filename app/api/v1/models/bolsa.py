from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from app.api.v1.utils.db import Base


class Bolsa(Base):
    __tablename__ = 'bolsas'
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String, unique=True, index=True)
    Megas=Column(Integer)
    cutting_day = Column(Integer)

    SIM = relationship('SIM', back_populates='bolsa')


