from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

from app.database.database import Base


class LoginHistory(Base):
    __tablename__ = "login_history"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    device_id = Column(String)

    browser = Column(String)

    ip_address = Column(String)

    decision = Column(String)

    risk_score = Column(Integer)

    trust_score = Column(Integer)

    created_at = Column(DateTime, default=datetime.utcnow)