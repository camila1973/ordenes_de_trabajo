# app/api/v1/utils/init_db.py

import os
from dotenv import load_dotenv
from pathlib import Path

# Carga .env.development desde el nivel del proyecto
dotenv_path = Path(__file__).resolve().parents[4] / ".env.development"
load_dotenv(dotenv_path)
print("dotenv_path: ", dotenv_path)
from app.api.v1.utils.db import Base, engine
from app.api.v1.models import user, role  # importa tus modelos

def init_db():
    print("🚀 Conectando y creando tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tablas creadas correctamente.")

if __name__ == "__main__":
    init_db()
