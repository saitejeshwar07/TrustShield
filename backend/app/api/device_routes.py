from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.device import DeviceCreate
from app.services.device_service import register_device

router = APIRouter(
    prefix="/api/device",
    tags=["Device"],
)


@router.post("/register")
def register(
    device: DeviceCreate,
    db: Session = Depends(get_db),
):
    return register_device(device, db)