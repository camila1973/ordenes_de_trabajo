from datetime import date

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from app.api.v1.utils.db import Base


class Bolsa(Base):
    __tablename__ = 'bolsa'
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String, unique=True, index=True)
    Megas=Column(Integer)
    cutting_day = Column(Integer)

    sims = relationship('SIM', back_populates='bolsa')

    @property
    def cutting_date(self) -> date:
        today = date.today()
        if today.day > self.cutting_day:
            if today.month == 12:
                return date(today.year + 1, 1, self.cutting_day)
            return date(today.year, today.month + 1, self.cutting_day)
        else:
            return date(today.year, today.month, self.cutting_day)



