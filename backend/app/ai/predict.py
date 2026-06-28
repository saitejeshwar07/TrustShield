import joblib
import pandas as pd

# Load trained model
model = joblib.load("app/ai/model.pkl")


def predict_login(
    new_device,
    new_browser,
    new_ip,
    login_hour,
):
    data = pd.DataFrame([{
        "new_device": int(new_device),
        "new_browser": int(new_browser),
        "new_ip": int(new_ip),
        "login_hour": login_hour,
    }])

    prediction = model.predict(data)

    if prediction[0] == -1:
        return "ANOMALY"

    return "NORMAL"

print(
    predict_login(
        new_device=True,
        new_browser=True,
        new_ip=True,
        login_hour=2,
    )
)