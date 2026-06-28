from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

from app.database.database import Base


class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    device_id = Column(String, nullable=False)

    browser = Column(String)

    operating_system = Column(String)

    screen_resolution = Column(String)

    timezone = Column(String)

    language = Column(String)

    ip_address = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)