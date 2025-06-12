from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import  OAuth2PasswordRequestForm
from sqlalchemy.orm import Session, joinedload

from app.api.v1.models.role import Role
from app.api.v1.models.user import User
from app.api.v1.schemas.user_schema import UserCreate, UserResponse, LoginResponse, LoginRequest
from app.api.v1.crud.user import create_user, verify_password, create_access_token, get_users
from app.api.v1.utils.db import get_db
from app.api.v1.utils.get_current_user import get_current_user

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
def listar_usuarios(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_users(db)


@router.post("/login", response_model=LoginResponse)
async def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
):
    # filter user
    user = db.query(User).options(joinedload(User.role)).filter(User.email == form_data.username).first()

    if not user:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    # Verify password
    if not verify_password(form_data.password, user.password_hash):
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