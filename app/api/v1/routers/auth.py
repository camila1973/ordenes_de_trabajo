from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

from app.api.v1.models.role import Role
from app.api.v1.models.user import User
from app.api.v1.schemas.user_schema import UserCreate, UserResponse, LoginResponse, LoginRequest
from app.api.v1.crud.user import create_user, verify_password, create_access_token, get_users
from app.api.v1.utils.db import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register", response_model=UserResponse)
async def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    try:
        new_user = create_user(db, user_data)
        return new_user
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Error interno del servidor"
        )

@router.get("/users", response_model=list[UserResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    return get_users(db)


@router.post("/login", response_model=LoginResponse)
async def login(
        login_data: LoginRequest,
        db: Session = Depends(get_db)
):
    # filter user
    user = db.query(User).options(joinedload(User.role)).filter(User.email == login_data.email).first()

    if not user:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    # Verify password
    if not verify_password(login_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    # token
    access_token = create_access_token(
        data={
            "sub": str(user.id),
            "email": user.email,
            "role": user.role.name if user.role else "user"
        }
    )

    return LoginResponse(
        access_token=access_token,
        user_id=user.id,
        email=user.email,
        role=user.role.name if user.role else "user"
    )

print("📦 auth router cargado")