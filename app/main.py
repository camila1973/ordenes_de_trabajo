import logging
import sys

from starlette.middleware.cors import CORSMiddleware

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

from fastapi import FastAPI
from app.api.v1.models import *

from app.api.v1.routers import auth, role, city, bolsa, sim, company, GPS

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #nota cambiar cuando este en desarrollo para recibir request de un solo front
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/ping")
def ping():
    return {"message": "pong"}

print("📦 Incluyendo routers...")
app.include_router(auth.router)

app.include_router(role.router)

app.include_router(city.router)

app.include_router(bolsa.router)

app.include_router(sim.router)

app.include_router(company.router)

app.include_router(GPS.router)