🚀 TrustShield AI

AI-Powered Identity Trust & Adaptive Authentication Platform

TrustShield AI is a production-inspired identity security platform that combines rule-based risk analysis with AI-powered anomaly detection to evaluate login attempts in real time. It continuously analyzes user behavior, device intelligence, browser information, IP changes, and login history to generate a Trust Score and determine whether a login should be Allowed, require Step-Up Authentication, or be Blocked.

✨ Features
🔐 Secure Authentication
JWT Authentication
Secure Password Hashing
User Registration & Login
Protected API Endpoints
🖥 Device Intelligence
Device Fingerprinting
Trusted Device Detection
Browser Detection
Operating System Detection
Screen Resolution Detection
Timezone Detection
Language Detection
IP Address Tracking
🧠 AI-Powered Risk Engine
Rule-Based Risk Analysis
Isolation Forest Anomaly Detection
Dynamic Trust Score Calculation
AI Prediction (Normal / Anomaly)
Adaptive Authentication Decisions
📊 Security Dashboard
Trust Score
Risk Score
AI Detection
Current Device
Decision Engine
Recent Login Activity
📜 Login History
Login Tracking
Browser History
Device History
Risk History
Trust Score History
🏗 System Architecture
                     React Frontend
                           │
                           ▼
                  FastAPI REST API
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
 Authentication      Identity Engine    Dashboard APIs
        │                  │                  │
        └──────────────────┼──────────────────┘
                           ▼
                  Rule-Based Risk Engine
                           │
                           ▼
             Isolation Forest AI Model
                           │
                           ▼
                  Trust Score Engine
                           │
                           ▼
                 Supabase PostgreSQL
🤖 AI Pipeline
User Login
     │
     ▼
Collect Device Information
     │
     ▼
Browser Detection
     │
     ▼
IP Detection
     │
     ▼
Rule-Based Risk Engine
     │
     ▼
Isolation Forest AI
     │
     ▼
AI Prediction
     │
     ▼
Trust Score
     │
     ▼
ALLOW / STEP_UP_AUTH / BLOCK
📸 Dashboard
Login
Secure Login
JWT Authentication
Responsive UI
Dashboard
Trust Score
Risk Score
AI Detection
Current Device
Decision Card
Recent Login History
AI Detection

The platform uses Isolation Forest to classify login attempts as:

✅ NORMAL
⚠️ ANOMALY
🧠 Risk Engine

Current Risk Factors:

Risk Factor	Score
New Device	+30
New Browser	+10
New IP Address	+20
New Country	+25
Unusual Login Time	+15
Multiple Failed Attempts	+40
Trusted Device	-20
🛠 Tech Stack
Frontend
React 19
Vite
Tailwind CSS
React Router
Axios
Framer Motion
Lucide React
Backend
FastAPI
SQLAlchemy
JWT Authentication
Passlib
Uvicorn
Database
Supabase PostgreSQL
Artificial Intelligence
Scikit-learn
Isolation Forest
Pandas
Joblib
📂 Project Structure
TrustShield/

├── backend/
│
│   ├── app/
│   │
│   ├── ai/
│   │   ├── generate_dataset.py
│   │   ├── train_model.py
│   │   ├── predict.py
│   │   └── model.pkl
│   │
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── risk_engine/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── frontend/
│
│   ├── src/
│   │
│   ├── components/
│   ├── pages/
│   ├── services/
│   ├── hooks/
│   └── App.jsx
│
├── docs/
└── README.md
🚀 Installation
Backend
git clone https://github.com/<your-username>/TrustShield.git

cd TrustShield/backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload

Backend runs on:

http://127.0.0.1:8000

Swagger:

http://127.0.0.1:8000/docs
Frontend
cd frontend

npm install

npm run dev

Runs on:

http://localhost:5173
🔌 API Endpoints
Method	Endpoint	Description
POST	/api/auth/register	Register User
POST	/api/auth/login	Login User
POST	/api/device/register	Register Device
POST	/api/identity/evaluate	Evaluate Login Risk
GET	/api/dashboard/summary	Dashboard Summary
GET	/api/dashboard/recent-logins	Login History
📊 AI Model

Algorithm:

Isolation Forest

Features Used:

New Device
New Browser
New IP Address
Login Hour

Output:

NORMAL

or

ANOMALY
🎯 Future Roadmap
Browser Fingerprinting
Geolocation Intelligence
Timezone-Based Risk Detection
Behavioral Biometrics
Real-Time Security Alerts
Admin Security Dashboard
Live Risk Analytics
Multi-Factor Authentication
Explainable AI (XAI)
Cloud Deployment
👨‍💻 Author

Pawar Sai Tejeshwar

B.Tech, Chemical Engineering
IIT Gandhinagar
📄 License

This project is released under the MIT License.

