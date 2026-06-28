import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest

# Load generated dataset
df = pd.read_csv("app/ai/login_dataset.csv")

# Use only features (ignore label column)
X = df[[
    "new_device",
    "new_browser",
    "new_ip",
    "login_hour",
]]

# Train Isolation Forest
model = IsolationForest(
    contamination=0.2,
    random_state=42,
)

model.fit(X)

# Save trained model
joblib.dump(model, "app/ai/model.pkl")

print("✅ AI Model Trained Successfully!")
print(f"Training Samples: {len(X)}")