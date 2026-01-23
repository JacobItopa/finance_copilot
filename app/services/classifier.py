from app.services.rag_context import get_company_context
from app.services.rule_categorizer import rule_based_category
from app.services.llm_categorizer import llm_categorize
from app.db.database import SessionLocal


def classify_transaction(transaction):
    rule_result = rule_based_category(transaction.description)
    if rule_result:
        transaction.category = rule_result["category"]
        transaction.confidence = rule_result["confidence"]
        transaction.classified_by = rule_result["classified_by"]
        return transaction

    db = SessionLocal()
    context = get_company_context(db)
    db.close()

    llm_result = llm_categorize(transaction.description, context)
    transaction.category = llm_result["category"]
    transaction.confidence = llm_result["confidence"]
    transaction.classified_by = llm_result["classified_by"]

    return transaction
