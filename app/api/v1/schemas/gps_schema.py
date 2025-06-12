from pydantic import BaseModel

from app.api.v1.schemas.branGps_schema import BrandGpsOut
from app.api.v1.schemas.sim_schema import SimOut


class GpsCreate(BaseModel):
    GPSid: str
    IMEI: str
    brand_id: int
    sim_id: int
    class Config:
        from_attributes = True

class GpsResponse(BaseModel):
    GPSid: str
    IMEI: str
    brand_id: int
    sim_id: int
    class Config:
        from_attributes = True

class GpsOut(BaseModel):
    id: int
    GPSid: str
    IMEI: str
    brand_id: BrandGpsOut
    sim_id: SimOut
    class Config:
        from_attributes = True