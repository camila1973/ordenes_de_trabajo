from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.api.v1.utils.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,  index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)

    role_id = Column(Integer, ForeignKey('roles.id'))
    role = relationship("Role", back_populates="users")


class Role:
    pass