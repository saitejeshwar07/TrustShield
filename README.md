🛡️ TrustShield AI








🚀 Overview

TrustShield AI is an AI-powered identity verification and risk-based authentication system that analyzes login behavior in real-time.

It combines:

🧠 Machine Learning (Isolation Forest)
📊 Rule-Based Risk Engine
🔐 Device Intelligence
🌐 Browser & IP Tracking
📈 Trust Score System

to decide whether a login should be:

✅ ALLOW
⚠️ STEP-UP AUTHENTICATION
❌ BLOCK
🎯 Problem It Solves

Modern systems struggle with:

Fake logins
Credential stuffing
Suspicious device access
Session hijacking

TrustShield AI solves this by continuously analyzing behavioral login signals instead of just passwords.

⚙️ Core Features
🔐 Authentication System
JWT-based login
Secure password hashing
User session management
🧠 AI Risk Engine
Isolation Forest anomaly detection
Behavioral pattern learning
Login anomaly classification
📊 Risk Scoring System
New device detection
Browser change detection
IP change detection
Login time analysis
🖥️ Device Intelligence
Device fingerprinting
OS detection
Browser tracking
📜 Login Monitoring
Full login history tracking
Risk logs per session
Trust score tracking
🏗️ System Architecture
Frontend (React)
      ↓
FastAPI Backend
      ↓
Risk Engine + AI Model
      ↓
PostgreSQL (Supabase)
🤖 AI Workflow
Login Request
     ↓
Feature Extraction
     ↓
Rule-Based Engine
     ↓
Isolation Forest Model
     ↓
Risk Score Calculation
     ↓
Final Decision

---

# 🛠 Tech Stack

## Frontend

| Technology | Purpose |
|------------|---------|
| React.js | User Interface |
| Vite | Build Tool |
| Tailwind CSS | Styling |
| React Router | Routing |
| Axios | API Requests |
| Framer Motion | Animations |
| Lucide React | Icons |

---

## Backend

| Technology | Purpose |
|------------|---------|
| FastAPI | REST API |
| SQLAlchemy | ORM |
| Pydantic | Data Validation |
| JWT | Authentication |
| Passlib | Password Hashing |
| Uvicorn | ASGI Server |

---

## Database

- PostgreSQL (Supabase)

---

## Artificial Intelligence

- Scikit-Learn
- Isolation Forest
- Pandas
- NumPy
- Joblib

---

# 📂 Project Structure

```text
TrustShield/
│
├── backend/
│   │
│   ├── app/
│   │   │
│   │   ├── ai/
│   │   │   ├── generate_dataset.py
│   │   │   ├── train_model.py
│   │   │   ├── train_from_db.py
│   │   │   ├── predict.py
│   │   │   ├── login_dataset.csv
│   │   │   └── model.pkl
│   │   │
│   │   ├── api/
│   │   ├── core/
│   │   ├── database/
│   │   ├── events/
│   │   ├── models/
│   │   ├── risk_engine/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   │
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── hooks/
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
├── README.md
└── .gitignore
```

---

# ⚡ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/TrustShield.git

cd TrustShield
```

---

## Backend Setup

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate

pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file inside the `backend` directory.

```env
DATABASE_URL=YOUR_DATABASE_URL

SECRET_KEY=YOUR_SECRET_KEY

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

## Run Backend

```bash
uvicorn app.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend URL

```
http://localhost:5173
```

---

# 🔑 Environment Requirements

- Python 3.11+
- Node.js 20+
- PostgreSQL (Supabase)
- Git
---

# 🔌 REST API Endpoints

## Authentication APIs

| Method | Endpoint | Description |
|----------|---------------------------|-------------------------|
| POST | `/api/auth/register` | Register a new user |
| POST | `/api/auth/login` | User login |

---

## Device APIs

| Method | Endpoint | Description |
|----------|---------------------------|---------------------------|
| POST | `/api/device/register` | Register a trusted device |

---

## Identity APIs

| Method | Endpoint | Description |
|----------|-------------------------------|---------------------------|
| POST | `/api/identity/evaluate` | Evaluate login risk |

---

## Dashboard APIs

| Method | Endpoint | Description |
|----------|-------------------------------|---------------------------|
| GET | `/api/dashboard/summary` | Dashboard summary |
| GET | `/api/dashboard/recent-logins` | Recent login history |

---

# 🤖 AI Pipeline

The AI engine uses **Isolation Forest** to identify anomalous login behavior.

```text
Login Attempt
      │
      ▼
Collect Device Information
      │
      ▼
Extract Login Features
      │
      ▼
Rule-Based Risk Engine
      │
      ▼
Isolation Forest Model
      │
      ▼
AI Prediction
      │
      ▼
Trust Score Calculation
      │
      ▼
ALLOW / STEP_UP_AUTH / BLOCK
```

---

# 🧠 Rule-Based Risk Engine

The platform combines traditional cybersecurity rules with AI.

Current risk factors include:

| Risk Factor | Risk Score |
|--------------|-----------:|
| New Device | +30 |
| New Browser | +10 |
| New IP Address | +20 |
| New Country | +25 |
| Unusual Login Time | +15 |
| Multiple Failed Attempts | +40 |
| Trusted Device | -20 |

---

# 🧠 AI Anomaly Detection

Machine Learning Model

```
Isolation Forest
```

Training Features

- New Device
- Browser Change
- IP Address Change
- Login Hour

Model Output

```
NORMAL
```

or

```
ANOMALY
```

If an anomaly is detected, the Risk Engine automatically increases the login risk score before generating the final authentication decision.

---

# 📊 Dashboard

The security dashboard provides a real-time overview of every login attempt.

### Dashboard Modules

- ✅ Trust Score
- ⚠ Risk Score
- 🤖 AI Detection
- 💻 Current Device
- 🌐 Browser Information
- 🔐 Authentication Decision
- 📜 Recent Login Activity

---

# 📸 Screenshots

## Login Page

```
docs/login.png
```

---

## Dashboard

```
docs/dashboard.png
```

---

## AI Detection

```
docs/ai_detection.png
```

---

## Login History

```
docs/login_history.png
```

> Replace these placeholders with actual screenshots from your project after deployment.

---

# 🔒 Security Features

- JWT Authentication
- Password Hashing
- Device Fingerprinting
- Trusted Device Detection
- Browser Tracking
- IP Address Monitoring
- Login History Tracking
- AI-Based Risk Analysis
- Adaptive Authentication
- PostgreSQL Data Storage

---

# 📈 Performance

Current TrustShield AI provides:

- Real-time login evaluation
- AI-assisted anomaly detection
- Dynamic trust score calculation
- FastAPI REST APIs
- Responsive React Dashboard
- Secure PostgreSQL storage

---
---

# 🚀 Future Roadmap

TrustShield AI is designed to evolve into a production-grade Identity Trust Platform.

## Phase 1 ✅
- JWT Authentication
- Device Registration
- Device Fingerprinting
- Rule-Based Risk Engine
- Login History
- Trust Score System

---

## Phase 2 ✅
- Browser Detection
- IP Address Detection
- AI Anomaly Detection
- Isolation Forest Model
- Security Dashboard

---

## Phase 3 🚧
- Geo-location Intelligence
- Timezone Analysis
- Adaptive Multi-Factor Authentication
- Email Security Alerts
- Risk Trend Analytics

---

## Phase 4 🎯
- Explainable AI (XAI)
- Continuous Authentication
- Behavioral Biometrics
- Mobile Application
- Enterprise Admin Dashboard

---

# 💡 Potential Applications

TrustShield AI can be integrated into:

- 🏦 Banking Applications
- 💳 FinTech Platforms
- 🏥 Healthcare Systems
- 🏛 Government Portals
- 🎓 University Portals
- 🛒 E-Commerce Platforms
- ☁ Cloud Platforms
- 🔐 Enterprise Identity Management

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve TrustShield AI:

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/your-feature
```

3. Commit your changes

```bash
git commit -m "feat: add awesome feature"
```

4. Push to your branch

```bash
git push origin feature/your-feature
```

5. Open a Pull Request

---

# 🧪 Future AI Improvements

- Deep Learning Based Risk Detection
- LSTM Login Behavior Prediction
- Autoencoder Anomaly Detection
- Explainable AI
- Reinforcement Learning Risk Scoring

---

# 📊 Project Status

| Module | Status |
|---------|--------|
| Authentication | ✅ Complete |
| Device Intelligence | ✅ Complete |
| Risk Engine | ✅ Complete |
| AI Detection | ✅ Complete |
| Dashboard | ✅ Complete |
| Login History | ✅ Complete |
| Browser Detection | ✅ Complete |
| IP Detection | ✅ Complete |
| API Integration | ✅ Complete |
| Deployment | 🚧 In Progress |

---

# 👨‍💻 Author

## Pawar Sai Tejeshwar

**B.Tech, Chemical Engineering**  
**Indian Institute of Technology Gandhinagar**

### Connect with me

- GitHub: https://github.com/YOUR_GITHUB_USERNAME
- LinkedIn: https://linkedin.com/in/YOUR_LINKEDIN_USERNAME
- Email: YOUR_EMAIL

---

# ⭐ Support

If you found this project useful:

⭐ Star this repository

🍴 Fork the repository

🐛 Report issues

💡 Suggest improvements

---

# 📄 License

This project is licensed under the **MIT License**.

See the **LICENSE** file for more information.

---

# 🙏 Acknowledgements

Special thanks to the open-source community and the developers behind:

- React
- FastAPI
- SQLAlchemy
- Supabase
- Scikit-learn
- Pandas
- Vite
- Tailwind CSS
- Framer Motion

---

<div align="center">

## 🛡️ TrustShield AI

### **Building Smarter Identity Security with Artificial Intelligence**

**⭐ If you like this project, don't forget to star the repository! ⭐**

Made with ❤️ by **Pawar Sai Tejeshwar**

</div>