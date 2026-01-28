from datetime import date
from app.agents.insight_agent import generate_insights
from app.agents.recommendation_agent import generate_recommendations
from app.routes.summary import financial_summary


def generate_daily_digest():
    insights = generate_insights()
    recommendations = generate_recommendations(insights)
    summary_data = financial_summary()

    alerts = []
    for insight in insights:
        if insight["severity"] in ["high", "medium"]:
            alerts.append(insight["description"])

    digest = {
        "date": date.today().isoformat(),
        "summary": "Here is your financial overview for today.",
        "key_metrics": {
            "total_income": summary_data["total_income"],
            "total_expense": summary_data["total_expense"],
            "net_cash_flow": summary_data["net_cash_flow"]
        },
        "alerts": alerts,
        "recommendations": [
            f"{rec.title}: {rec.action}" for rec in recommendations
        ]
    }

    return digest
