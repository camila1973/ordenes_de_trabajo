from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.api.v1.utils.db import Base


class TechnicalOffice(Base):
    __tablename__='technical_offices'

    id=Column(Integer , primary_key=True , index=True)
    name=Column(String, index=True)

    city_id=Column(Integer, ForeignKey('cities.id'))
    city=relationship("City", back_populates="technical_offices")
