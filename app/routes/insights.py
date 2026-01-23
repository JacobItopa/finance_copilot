from fastapi import APIRouter
from app.agents.insight_agent import generate_insights

router = APIRouter(prefix="/insights", tags=["Insights"])

@router.get("/")
def get_insights():
    insights = generate_insights()
    return {"insights": insights}
