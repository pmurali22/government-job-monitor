import smtplib
from email.message import EmailMessage
from app.config import settings

class EmailService:
    def send_email(self, recipient: str, subject: str, content: str):
        msg = EmailMessage()
        msg['From'] = settings.EMAIL_FROM
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.set_content(content)
        with smtplib.SMTP('localhost') as smtp:
            smtp.send_message(msg)
