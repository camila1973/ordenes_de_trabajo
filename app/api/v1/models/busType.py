from sqlalchemy import Column, Integer, String
from app.api.v1.utils.db import Base


class BusType(Base):
    __tablename__ = 'busTypes'
    id= Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

