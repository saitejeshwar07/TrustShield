import random
import pandas as pd

random.seed(42)

records = []

devices = [
    "Windows",
    "Mac",
    "Android",
    "Linux"
]

browsers = [
    "Chrome",
    "Edge",
    "Firefox",
    "Safari"
]

ips = [
    "192.168.1.100",
    "192.168.1.101",
    "10.0.0.1",
    "172.16.1.20"
]

for _ in range(1000):

    # 80% Normal Logins
    if random.random() < 0.8:

        new_device = 0
        new_browser = 0
        new_ip = 0
        login_hour = random.randint(8, 22)
        label = "Normal"

    # 20% Suspicious Logins
    else:

        new_device = random.randint(0, 1)
        new_browser = random.randint(0, 1)
        new_ip = random.randint(0, 1)
        login_hour = random.choice([0, 1, 2, 3, 4, 5])

        label = "Anomaly"

    records.append({
        "new_device": new_device,
        "new_browser": new_browser,
        "new_ip": new_ip,
        "login_hour": login_hour,
        "label": label
    })

df = pd.DataFrame(records)

df.to_csv("app/ai/login_dataset.csv", index=False)

print("✅ Dataset Generated Successfully")
print(df.head())
print(f"\nTotal Records: {len(df)}")