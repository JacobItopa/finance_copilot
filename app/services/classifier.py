from app.services.rule_categorizer import rule_based_category
from app.services.llm_categorizer import llm_categorize


def classify_transaction(transaction):
    rule_result = rule_based_category(transaction.description)

    if rule_result:
        transaction.category = rule_result["category"]
        transaction.confidence = rule_result["confidence"]
        transaction.classified_by = rule_result["classified_by"]
        return transaction

    # fallback to LLM
    llm_result = llm_categorize(transaction.description)
    transaction.category = llm_result["category"]
    transaction.confidence = llm_result["confidence"]
    transaction.classified_by = llm_result["classified_by"]

    return transaction
