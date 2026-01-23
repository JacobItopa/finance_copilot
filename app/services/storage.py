from app.db.database import SessionLocal
from app.db.models import TransactionDB


def save_transactions(transactions):
    db = SessionLocal()
    for tx in transactions:
        record = TransactionDB(**tx.dict())
        db.merge(record)
    db.commit()
    db.close()
