import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest

from app.database.database import SessionLocal
from app.models.login_history import LoginHistory

# Create database session
db = SessionLocal()

# Fetch login history
logins = db.query(LoginHistory).all()

# Close session
db.close()

# If there isn't enough data, stop
if len(logins) < 10:
    print("❌ Not enough login history to train the model.")
    print(f"Current records: {len(logins)}")
    exit()

# Prepare training data
data = []

for login in logins:
    data.append({
        "new_device": 1 if "windows" in login.device_id.lower() else 0,
        "new_browser": 1 if login.browser.lower() != "chrome" else 0,
        "new_ip": 1 if login.ip_address != "192.168.1.100" else 0,
        "login_hour": login.created_at.hour,
    })

df = pd.DataFrame(data)

# Train AI model
model = IsolationForest(
    contamination=0.1,
    random_state=42
)

model.fit(df)

# Save model
joblib.dump(model, "app/ai/model.pkl")

print("✅ AI model trained using database login history.")