from sqlalchemy.orm import Session
from app.db.models import TransactionDB


def get_company_context(db: Session, limit=50):
    txs = db.query(TransactionDB).order_by(
        TransactionDB.date.desc()
    ).limit(limit).all()

    summaries = []
    for tx in txs:
        summaries.append(
            f"{tx.description} → {tx.category}"
        )

    return "\n".join(summaries)
