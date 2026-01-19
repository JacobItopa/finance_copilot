import pandas as pd
from uuid import uuid4
from app.schemas.transaction import Transaction


def parse_csv(file_path: str) -> list[Transaction]:
    df = pd.read_csv(file_path)

    required_columns = {"date", "description", "amount", "direction", "currency"}
    if not required_columns.issubset(df.columns):
        raise ValueError("CSV missing required columns")

    transactions = []

    for _, row in df.iterrows():
        transaction = Transaction(
            transaction_id=str(uuid4()),
            date=row["date"],
            description=row["description"],
            amount=float(row["amount"]),
            direction=row["direction"].lower(),
            currency=row["currency"]
        )
        transactions.append(transaction)

    return transactions
