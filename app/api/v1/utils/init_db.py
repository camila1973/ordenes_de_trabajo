from dotenv import load_dotenv
from pathlib import Path
from app.api.v1.utils.db import Base, engine
from app.api.v1.utils.settings import settings

# Carga .env.development desde el nivel del proyecto
dotenv_path = Path(__file__).resolve().parents[4] / ".env.development"
load_dotenv(dotenv_path)
print("dotenv_path: ", dotenv_path)
from app.api.v1.models.user import User
from app.api.v1.models.role import Role

def init_db():
    print("🚀 Conectando y creando tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tablas creadas correctamente.")
    print("Loaded DB_USER:", settings.db_user)
if __name__ == "__main__":
    init_db()
