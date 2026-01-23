from app.db.database import SessionLocal
from app.db.models import TransactionDB
from datetime import datetime, timedelta

def detect_anomalies():
    db = SessionLocal()
    txs = db.query(TransactionDB).all()
    db.close()

    # Calculate average expense per category
    category_totals = {}
    category_counts = {}

    for tx in txs:
        if tx.direction == "debit":
            cat = tx.category or "Uncategorized"
            category_totals[cat] = category_totals.get(cat, 0) + tx.amount
            category_counts[cat] = category_counts.get(cat, 0) + 1

    anomalies = []

    for tx in txs:
        if tx.direction != "debit":
            continue
        cat = tx.category or "Uncategorized"
        avg = category_totals[cat] / category_counts[cat]

        # Flag if transaction > 2x category average
        if tx.amount > 2 * avg:
            anomalies.append({
                "transaction_id": tx.transaction_id,
                "category": cat,
                "amount": tx.amount,
                "severity": "high",
                "description": f"Transaction {tx.description} is unusually high for {cat}"
            })

    return anomalies
