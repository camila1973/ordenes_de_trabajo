from sqlalchemy import Table, Column, Integer, ForeignKey

from app.api.v1.utils.db import Base

company_owner = Table(
    'company_owner',
    Base.metadata,
    Column('company_id', Integer, ForeignKey('companies.id'), primary_key=True),
    Column('owner_id', Integer, ForeignKey('owners.id'), primary_key=True)
)
