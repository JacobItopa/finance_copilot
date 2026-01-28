def render_daily_digest_email(digest: dict):
    alerts_html = "".join(
        f"<li>{alert}</li>" for alert in digest["alerts"]
    ) or "<li>No critical alerts today 🎉</li>"

    recommendations_html = "".join(
        f"<li>{rec}</li>" for rec in digest["recommendations"]
    )

    return f"""
    <html>
        <body style="font-family: Arial, sans-serif;">
            <h2>📊 Daily Financial Digest</h2>
            <p>{digest["summary"]}</p>

            <h3>Key Metrics</h3>
            <ul>
                <li>Total Income: {digest["key_metrics"]["total_income"]}</li>
                <li>Total Expense: {digest["key_metrics"]["total_expense"]}</li>
                <li>Net Cash Flow: {digest["key_metrics"]["net_cash_flow"]}</li>
            </ul>

            <h3>⚠️ Alerts</h3>
            <ul>{alerts_html}</ul>

            <h3>✅ Recommendations</h3>
            <ul>{recommendations_html}</ul>

            <p style="margin-top:20px;color:#666;">
                Sent by SME Financial Intelligence Copilot
            </p>
        </body>
    </html>
    """
