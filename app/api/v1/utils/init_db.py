from dotenv import load_dotenv
from pathlib import Path

from sqlalchemy.orm import Session

from app.api.v1.utils.db import Base, engine, SessionLocal
from app.api.v1.utils.settings import settings

# Carga .env.development desde el nivel del proyecto
dotenv_path = Path(__file__).resolve().parents[4] / ".env.development"
load_dotenv(dotenv_path)
print("dotenv_path: ", dotenv_path)

from app.api.v1.models.user import User
from app.api.v1.models.SIM import SIM
from app.api.v1.models.role import Role
from app.api.v1.models.bolsa import Bolsa
from app.api.v1.models.brandGps import Brand
from app.api.v1.models.city import City
from app.api.v1.models.company import Company
from app.api.v1.models.equipment import Equipment
from app.api.v1.models.firmware import Firmware
from app.api.v1.models.GPS import GPS
from app.api.v1.models.owner import Owner
from app.api.v1.models.company_owner import company_owner
from app.api.v1.models.busType import BusType


from app.api.v1.models.technical_office import TechnicalOffice

def init_db():
    print("Conectando y creando tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas correctamente.")
    print("Loaded DB_USER:", settings.db_user)

    db: Session = SessionLocal()

    try:
        seed_roles = ['admin', 'tecnico', 'contable']
        for role_name in seed_roles:
            exists = db.query(Role).filter_by(name=role_name).first()
            if not exists:
                new_role = Role(name=role_name)
                db.add(new_role)
                print(f"🟢 Rol '{role_name}' insertado.")
            else:
                print(f"🟡 Rol '{role_name}' ya existe.")

        db.commit()
    except Exception as e:
        print("❌ Error al insertar roles:", e)
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    init_db()
