from sqlalchemy.orm import Session
from app.models.login_history import LoginHistory


def save_login(
    user_id: int,
    device_id: str,
    browser: str,
    ip_address: str,
    decision: str,
    risk_score: int,
    trust_score: int,
    db: Session,
):
    login = LoginHistory(
        user_id=user_id,
        device_id=device_id,
        browser=browser,
        ip_address=ip_address,
        decision=decision,
        risk_score=risk_score,
        trust_score=trust_score,
    )

    db.add(login)
    db.commit()
    db.refresh(login)

    return login


def get_recent_logins(user_id: int, db: Session, limit: int = 10):
    return (
        db.query(LoginHistory)
        .filter(LoginHistory.user_id == user_id)
        .order_by(LoginHistory.created_at.desc())
        .limit(limit)
        .all()
    )