from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.db.models import TransactionDB

router = APIRouter(prefix="/summary", tags=["Summary"])


@router.get("/")
def financial_summary():
    db: Session = SessionLocal()

    txs = db.query(TransactionDB).all()
    db.close()

    total_income = sum(
        tx.amount for tx in txs if tx.direction == "credit"
    )
    total_expense = sum(
        tx.amount for tx in txs if tx.direction == "debit"
    )

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "net_cash_flow": total_income - total_expense
    }
