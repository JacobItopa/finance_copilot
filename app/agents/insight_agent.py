from app.agents.anomaly_agent import detect_anomalies
from app.agents.runway_agent import estimate_cash_runway

def generate_insights():
    anomalies = detect_anomalies()
    runway = estimate_cash_runway()

    insights = []

    # Cash runway insight
    insights.append({
        "type": "cash_runway",
        "severity": runway["risk"],
        "description": f"Estimated cash runway is {runway['runway_days']} days."
    })

    # Anomaly insights
    for a in anomalies:
        insights.append({
            "type": "anomaly",
            "severity": a["severity"],
            "description": a["description"]
        })

    return insights
