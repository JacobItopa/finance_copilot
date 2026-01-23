from app.db.database import SessionLocal
from app.db.models import TransactionDB

def estimate_cash_runway():
    db = SessionLocal()
    txs = db.query(TransactionDB).all()
    db.close()

    if not txs:
        return {
            "net_cash": 0,
            "daily_burn": 0,
            "runway_days": 0,
            "risk": "high"
        }

    total_income = sum(tx.amount for tx in txs if tx.direction == "credit")
    total_expense = sum(tx.amount for tx in txs if tx.direction == "debit")
    net_cash = total_income - total_expense

    # Estimate average daily burn
    days = max((max(tx.date for tx in txs) - min(tx.date for tx in txs)).days, 1)
    daily_burn = total_expense / days

    if daily_burn == 0:
        runway_days = float('inf')
    else:
        runway_days = net_cash / daily_burn

    return {
        "net_cash": net_cash,
        "daily_burn": daily_burn,
        "runway_days": round(runway_days, 2),
        "risk": "low" if runway_days > 60 else "medium" if runway_days > 30 else "high"
    }
