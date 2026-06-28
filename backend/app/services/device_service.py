from sqlalchemy.orm import Session
from app.models.device import Device


def register_device(device, db: Session):
    existing = (
        db.query(Device)
        .filter(
            Device.user_id == device.user_id,
            Device.device_id == device.device_id,
        )
        .first()
    )

    if existing:
        return {
            "trusted": True,
            "message": "Known device"
        }

    new_device = Device(**device.model_dump())

    db.add(new_device)
    db.commit()
    db.refresh(new_device)   # Optional but recommended

    return {
        "trusted": False,
        "message": "New device registered"
    }


def is_trusted_device(user_id: int, device_id: str, db: Session) -> bool:
    device = (
        db.query(Device)
        .filter(
            Device.user_id == user_id,
            Device.device_id == device_id,
        )
        .first()
    )

    return device is not None