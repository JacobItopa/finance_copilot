from app.agents.digest_agent import generate_daily_digest
from app.services.email_service import send_email
from app.templates.daily_digest_email import render_daily_digest_email


def send_daily_digest_email(user_email: str):
    digest = generate_daily_digest()
    html = render_daily_digest_email(digest)

    send_email(
        to_email=user_email,
        subject="Your Daily Financial Digest",
        html_content=html
    )

    return {
        "status": "sent",
        "email": user_email
    }
