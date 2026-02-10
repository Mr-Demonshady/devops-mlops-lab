import os
import traceback
import smtplib
from email.message import EmailMessage

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import mlflow
import mlflow.sklearn
from dotenv import load_dotenv


def send_failure_email(subject: str, body: str) -> None:
    """Send email alert only when called (i.e., on failure)."""
    load_dotenv()

    host = os.getenv("EMAIL_HOST", "smtp.gmail.com")
    port = int(os.getenv("EMAIL_PORT", "587"))
    user = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    to_email = os.getenv("EMAIL_TO", user)

    if not user or not password or not to_email:
        print("Email not sent: EMAIL_USER/EMAIL_PASS/EMAIL_TO not set in .env")
        return

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = user
    msg["To"] = to_email
    msg.set_content(body)

    with smtplib.SMTP(host, port) as server:
        server.starttls()
        server.login(user, password)
        server.send_message(msg)


def main():
    try:
        # ✅ MLflow stable backend
        mlflow.set_tracking_uri("sqlite:///mlflow.db")
        mlflow.set_experiment("DevOps-MLOps-Lab")

        # Load dataset
        data = pd.read_csv("data/dataset.csv")
        data.columns = data.columns.str.strip().str.lower()

        required_cols = {"feature", "label"}
        if not required_cols.issubset(set(data.columns)):
            raise ValueError(f"Dataset must contain columns {required_cols}, got {set(data.columns)}")

        X = data[["feature"]]
        y = data["label"]

        with mlflow.start_run():
            model = LinearRegression()
            model.fit(X, y)

            preds = model.predict(X)
            mse = mean_squared_error(y, preds)

            mlflow.log_metric("mse", mse)
            mlflow.sklearn.log_model(model, "linear_model")

            print("Training completed successfully")
            print("MSE:", mse)

    except Exception as e:
        # ✅ Email only on failure
        err_text = traceback.format_exc()
        print("ERROR: Training failed\n", err_text)

        send_failure_email(
            subject="DevOps-MLOps Lab FAILED: train.py error",
            body=f"Training failed.\n\nError:\n{err_text}"
        )

        # Re-raise so CI/CD also fails (required)
        raise


if __name__ == "__main__":
    main()
