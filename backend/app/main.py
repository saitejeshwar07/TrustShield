from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import Base, engine

from app.models.user import User
from app.models.device import Device
from app.models.login_history import LoginHistory

from app.api.auth_routes import router as auth_router
from app.api.device_routes import router as device_router
from app.api.identity_routes import router as identity_router
from app.api.dashboard_routes import router as dashboard_router
from app.api.login_history_routes import router as login_history_router
from app.api.trusted_devices_routes import router as trusted_devices_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TrustShield AI",
    version="1.0.0",
    description="AI Powered Identity Trust Platform"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(device_router)
app.include_router(identity_router)
app.include_router(dashboard_router)
app.include_router(login_history_router)
app.include_router(trusted_devices_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to TrustShield AI 🚀"
    }