from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.responses import JSONResponse
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from routing.client_router import router as client_router
from app.client_service import ClientService
from models.client import ClientEntity

app = FastAPI()
# app.include_router(client_router)


class EmailSchema(BaseModel):
    subject: str
    message: str
    recipients: List[str]


@app.post("/send_email/")
async def send_email(email: EmailSchema):
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = ", ".join(email.recipients)
    message["Subject"] = email.subject

    message.attach(MIMEText(email.message, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, email.recipients, message.as_string())
    server.quit()

    return {"message": "Email sent successfully"}




if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
