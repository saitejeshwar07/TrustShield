from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.user import UserCreate, UserLogin
from app.auth.auth import register_user, login_user

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    return register_user(user, db)


@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db),
):
    return login_user(user, db)