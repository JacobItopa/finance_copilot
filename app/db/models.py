from sqlalchemy import Column, String, Float, Date
from app.db.database import Base


class TransactionDB(Base):
    __tablename__ = "transactions"

    transaction_id = Column(String, primary_key=True, index=True)
    date = Column(Date)
    description = Column(String)
    amount = Column(Float)
    direction = Column(String)
    currency = Column(String)
    category = Column(String)
    confidence = Column(Float)
    classified_by = Column(String)
