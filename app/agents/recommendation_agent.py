from app.schemas.recommendation import Recommendation


def generate_recommendations(insights: list[dict]) -> list[Recommendation]:
    recommendations = []

    for insight in insights:
        if insight["type"] == "cash_runway":
            if insight["severity"] == "high":
                recommendations.append(
                    Recommendation(
                        priority="critical",
                        title="Low Cash Runway",
                        action="Reduce discretionary spending and explore short-term financing options.",
                        rationale="Your estimated cash runway is below 30 days, which poses a high operational risk."
                    )
                )
            elif insight["severity"] == "medium":
                recommendations.append(
                    Recommendation(
                        priority="important",
                        title="Monitor Cash Burn",
                        action="Review recurring expenses and delay non-essential payments.",
                        rationale="Your current cash runway suggests tightening cash management."
                    )
                )

        if insight["type"] == "anomaly":
            recommendations.append(
                Recommendation(
                    priority="important",
                    title="Unusual Expense Detected",
                    action="Review this transaction and confirm whether it was expected.",
                    rationale=insight["description"]
                )
            )

    if not recommendations:
        recommendations.append(
            Recommendation(
                priority="info",
                title="Financial Health Stable",
                action="Continue monitoring your finances regularly.",
                rationale="No significant financial risks or anomalies were detected."
            )
        )

    return recommendations
