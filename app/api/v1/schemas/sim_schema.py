from pydantic import BaseModel
from app.api.v1.schemas.bolsa_schema import BolsaOut

class SimCreate(BaseModel):
    IMEI_sim: str
    phone:str
    bolsa_id:int
    class Config:
        from_attributes = True

class SimOut(BaseModel):
    id: int
    IMEI_sim: str
    phone:str
    bolsa:BolsaOut
