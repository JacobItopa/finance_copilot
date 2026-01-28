from fastapi import APIRouter
from app.agents.insight_agent import generate_insights
from app.agents.recommendation_agent import generate_recommendations

router = APIRouter(prefix="/recommendations", tags=["Recommendations"])


@router.get("/")
def get_recommendations():
    insights = generate_insights()
    recommendations = generate_recommendations(insights)

    return {
        "recommendations": recommendations
    }
