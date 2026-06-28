from sqlalchemy.orm import Session
from app.models.login_history import LoginHistory


def ip_changed(user_id: int, current_ip: str, db: Session) -> bool:
    last_login = (
        db.query(LoginHistory)
        .filter(LoginHistory.user_id == user_id)
        .order_by(LoginHistory.created_at.desc())
        .first()
    )

    if last_login is None:
        return False

    return last_login.ip_address != current_ip