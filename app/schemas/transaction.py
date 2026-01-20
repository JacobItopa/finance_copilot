from pydantic import BaseModel
from datetime import date
from typing import Optional, Literal


class Transaction(BaseModel):
    transaction_id: Optional[str]
    date: date
    description: str
    amount: float
    direction: Literal["credit", "debit"]
    currency: str

    category: Optional[str] = None
    confidence: Optional[float] = None
    classified_by: Optional[Literal["rules", "llm"]] = None
