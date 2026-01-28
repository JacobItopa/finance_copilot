from fastapi import APIRouter
from app.agents.email_digest_agent import send_daily_digest_email

router = APIRouter(prefix="/email-digest", tags=["Email Digest"])


@router.post("/")
def send_digest(email: str):
    return send_daily_digest_email(email)
