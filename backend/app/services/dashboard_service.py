from sqlalchemy.orm import Session
from app.models.login_history import LoginHistory


def get_dashboard_summary(user_id: int, db: Session):
    latest_login = (
        db.query(LoginHistory)
        .filter(LoginHistory.user_id == user_id)
        .order_by(LoginHistory.created_at.desc())
        .first()
    )

    if not latest_login:
        return {
            "trust_score": 100,
            "risk": 0,
            "decision": "ALLOW",
            "device": "Unknown",
            "browser": "Unknown",
            "status": "No Login History"
        }

    return {
        "trust_score": latest_login.trust_score,
        "risk": latest_login.risk_score,
        "decision": latest_login.decision,
        "device": latest_login.device_id,
        "browser": latest_login.browser,
        "status": "Trusted Device" if latest_login.trust_score >= 80 else "Review Required",
    }