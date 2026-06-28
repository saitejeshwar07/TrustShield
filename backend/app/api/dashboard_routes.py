from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services.dashboard_service import get_dashboard_summary
from app.services.login_history_service import get_recent_logins

router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"],
)


@router.get("/summary")
def dashboard_summary(
    db: Session = Depends(get_db),
):
    """
    Temporary: using user_id=1.
    Later we'll extract the user ID from the JWT.
    """
    return get_dashboard_summary(
        user_id=1,
        db=db,
    )
@router.get("/recent-logins")
def recent_logins(
    db: Session = Depends(get_db),
):
    logins = get_recent_logins(
        user_id=1,
        db=db,
    )

    return logins