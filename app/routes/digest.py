from fastapi import APIRouter
from app.agents.digest_agent import generate_daily_digest

router = APIRouter(prefix="/digest", tags=["Daily Digest"])


@router.get("/")
def get_daily_digest():
    return generate_daily_digest()
