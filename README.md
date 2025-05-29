# ordenes_de_trabajo

#  Ordenes de Trabajo - Backend con FastAPI

Este es un backend construido con **FastAPI** que gestiona órdenes de trabajo, autenticación de usuarios con **JWT**, y una base de datos **PostgreSQL**.

---

## Tecnologías utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [Docker](https://www.docker.com/)
- [JWT](https://jwt.io/)

---

## Requisitos previos

- Tener instalado [Docker](https://www.docker.com/)
- Tener instalado [Docker Compose](https://docs.docker.com/compose/)
- Opcional: Python 3.12+ si deseas ejecutar fuera de Docker

---

## Variables de entorno

Crea un archivo `.env.development` en la raíz del proyecto con el siguiente contenido:

```env
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=postgres
DB_PORT=5432
DB_NAME=ordenes
SECRET_KEY=tu_clave_super_secreta
ALGORITHM=algoritmo_del_token
ACCESS_TOKEN_EXPIRE_MINUTES=minutos
```

> ⚠️ Este archivo se usa tanto en el backend como en la inicialización de la base de datos.

---

## 🐳 Ejecución del proyecto con Docker

### 1. Construir e iniciar los contenedores

```bash
docker-compose up --build
```

Esto levantará:

- Un contenedor con PostgreSQL
- Un contenedor que inicializa la base de datos (se ejecuta una sola vez)
- Un contenedor con el backend FastAPI

### 2. Acceder a la documentación interactiva

Cuando esté corriendo, puedes visitar:

- **Swagger Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🧪 Endpoints disponibles

- `POST /auth/register` – Registrar usuario
- `POST /auth/login` – Login con JWT
- `GET /ping` – Endpoint de prueba

---

## 🗃️ Migraciones con Alembic

> Recomendado para aplicar cambios estructurales en la base de datos.

1. Crear una migración:

```bash
alembic revision --autogenerate -m "mensaje"
```

2. Aplicar migraciones:

```bash
alembic upgrade head
```

> Asegúrate de tener configurado correctamente el archivo `alembic.ini` y los modelos importados en `env.py`.

---

## ✅ Estado actual

- [x] Registro de usuarios
- [x] Autenticación con JWT
- [x] Conexión a PostgreSQL
- [x] Docker funcionando
- [ ] Migraciones con Alembic
- [ ] Tests automatizados

---

## 🧑‍💻 Autora

**Camila Guayara**  
| 💻 [GitHub](https://github.com/camila1973)
