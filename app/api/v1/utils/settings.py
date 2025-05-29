from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str
    secret_key: str

    class Config:
        env_file = ".env.development"
        env_file_encoding = "utf-8"

# Singleton de configuración
settings = Settings()
print("Loaded DB_USER:", settings.db_user)
