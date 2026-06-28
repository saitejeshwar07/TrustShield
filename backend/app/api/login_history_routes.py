from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services.login_history_service import get_recent_logins

router = APIRouter(
    prefix="/api/login-history",
    tags=["Login History"],
)


@router.get("/{user_id}")
def recent_logins(user_id: int, db: Session = Depends(get_db)):
    logins = get_recent_logins(user_id, db)

    return logins