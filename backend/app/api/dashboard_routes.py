from fastapi import APIRouter

router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"],
)


@router.get("/summary")
def dashboard_summary():
    return {
        "trust_score": 92,
        "risk": 18,
        "decision": "ALLOW",
        "device": "Windows 11",
        "browser": "Chrome",
        "status": "Trusted Device",
        "ai_prediction": "NORMAL",
        "model": "Isolation Forest",
    }