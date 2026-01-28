import os
import resend

resend.api_key = os.getenv("RESEND_API_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")


def send_email(to_email: str, subject: str, html_content: str):
    response = resend.Emails.send({
        "from": SENDER_EMAIL,
        "to": [to_email],
        "subject": subject,
        "html": html_content
    })
    return response
