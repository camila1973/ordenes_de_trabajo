from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.api.v1.crud.sim import create_sim, get_sims, update_sim
from app.api.v1.schemas.sim_schema import SimOut, SimCreate, SimUpdate
from app.api.v1.utils.db import get_db

router = APIRouter(prefix="/sims", tags=["SIMs"])

@router.get("/",response_model=list[SimOut])
def list_sims(db: Session = Depends(get_db)):
    return get_sims(db)

@router.post('/', response_model=SimCreate)
def crear_sim(sim: SimCreate, db: Session = Depends(get_db)):
    return create_sim(db, sim)
@router.put("/{sim_id}", response_model=SimUpdate)
def update_sim_endpoint(sim_id:int,sim:SimUpdate,db:Session=Depends(get_db)):
    return update_sim(db,sim_id,sim.dict(exclude_unset=True))
