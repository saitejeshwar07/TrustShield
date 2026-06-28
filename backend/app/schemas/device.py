from pydantic import BaseModel


class DeviceCreate(BaseModel):
    user_id: int
    device_id: str
    browser: str
    operating_system: str
    screen_resolution: str
    timezone: str
    language: str
    ip_address: str