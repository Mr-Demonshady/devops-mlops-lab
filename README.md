# DevOps and MLOps Pipeline Implementation

**Subject:** DevOps and MLOps  
**Subject Code:** PUSDSBAMAJ M5P2  
**Course:** B.Sc. Semester V – KT / Supplementary Examination  

---

## 📌 Objective

To implement an end-to-end **DevOps + MLOps pipeline** for a Python machine learning application using:

- GitHub & GitHub Actions (CI/CD)
- DVC (Dataset Versioning)
- MLflow (Experiment Tracking)
- Docker & Docker Compose
- Email alerts on failure

---

## 📂 Project Structure

devops-mlops-lab/
│
├── .github/workflows/
│ └── ci.yml
│
├── data/
│ ├── dataset.csv
│ └── dataset.csv.dvc
│
├── .dvc/
├── .gitignore
├── app.py
├── train.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md


---

## 🚀 Tools & Technologies Used

- **Python 3.12**
- **Git & GitHub**
- **GitHub Actions (CI/CD)**
- **DVC** – Dataset versioning
- **MLflow** – Experiment tracking
- **Docker & Docker Compose**
- **SQLite** – MLflow backend
- **VS Code**

---

## ⚙️ Running the Project Locally

### 1️⃣ Create virtual environment
```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows Git Bash
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Pull dataset using DVC
dvc pull
4️⃣ Run the training script
python train.py
📊 MLflow Experiment Tracking
Start MLflow UI
mlflow ui --backend-store-uri sqlite:///mlflow.db
Open in browser:

http://127.0.0.1:5000
✔ Experiment name: DevOps-MLOps-Lab
✔ Metric logged: Mean Squared Error (MSE)
✔ Model artifact: linear_model

🐳 Running Using Docker
Build Docker image
docker build -t devops-mlops-lab .
Run Docker container
docker run devops-mlops-lab
🐳 Docker Compose
docker-compose up --build
🔔 Email Alerts on Failure
Email alerts are triggered only on failure

Implemented using try-except

Email credentials stored securely using environment variables (.env)

🔁 CI/CD Pipeline
GitHub Actions pipeline performs:

Dependency installation

Python script execution

Docker image build attempt

Pipeline triggers automatically on every push.

📸 Screenshots Included (For Exam Submission)
GitHub repository (public)

GitHub Actions successful run

DVC dataset tracking

MLflow experiment with metric

Docker build/run output

Email failure alert proof

## CI/CD Pipeline

This project includes a GitHub Actions CI/CD pipeline that:
- Installs dependencies
- Runs the ML training pipeline
- Logs metrics and models using MLflow
- Builds a Docker image
- Fails the pipeline if training errors occur

The pipeline ensures reproducibility, automation, and early error detection.
