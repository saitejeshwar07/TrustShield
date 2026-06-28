from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.device import Device

router = APIRouter(
    prefix="/api/devices",
    tags=["Trusted Devices"],
)


@router.get("/")
def get_devices(
    db: Session = Depends(get_db),
):
    devices = (
        db.query(Device)
        .filter(Device.user_id == 1)   # Temporary
        .all()
    )

    return devices