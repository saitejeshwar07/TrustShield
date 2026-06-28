from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.device import DeviceCreate
from app.services.device_service import is_trusted_device
from app.services.login_history_service import save_login
from app.risk_engine.risk_service import evaluate_login
from app.services.browser_service import browser_changed
from app.services.risk_analyzer import analyze_login

router = APIRouter(
    prefix="/api/identity",
    tags=["Identity"],
)


@router.post("/evaluate")
def evaluate(
    device: DeviceCreate,
    db: Session = Depends(get_db),
):
    # Check whether the current device is trusted
    trusted = is_trusted_device(
        user_id=device.user_id,
        device_id=device.device_id,
        db=db,
    )

    # Calculate risk score
    result = evaluate_login(
        new_device=not trusted,
        new_country=False,
        new_browser=browser_changed(
        user_id=device.user_id,
        current_browser=device.browser,
        db=db,
    ),
        new_ip=False,
        unusual_login_time=False,
        failed_attempts=0,
        trusted_device=trusted,
    )

    # Save login history
    save_login(
        user_id=device.user_id,
        device_id=device.device_id,
        browser=device.browser,
        ip_address=device.ip_address,
        decision=result["decision"],
        risk_score=result["risk"],
        trust_score=result["trust_score"],
        db=db,
    )

    return {
        "trusted_device": trusted,
        "trust_score": result["trust_score"],
        "risk": result["risk"],
        "decision": result["decision"],
        "ai_prediction": result["ai_prediction"],
    }