from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)


def register_user(user: UserCreate, db: Session):
    # Check if email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        return {"error": "Email already registered"}

    # Create new user
    new_user = User(
        full_name=user.full_name,
        email=user.email,
        password=hash_password(user.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "user": new_user,
    }


def login_user(user: UserLogin, db: Session):

    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        return {"error": "Invalid email or password"}

    if not verify_password(user.password, db_user.password):
        return {"error": "Invalid email or password"}

    token = create_access_token(
        {
            "sub": db_user.email,
            "id": db_user.id,
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }