import re

CATEGORY_RULES = {
    "Revenue": [r"stripe", r"payment received", r"payout"],
    "Rent": [r"rent", r"lease"],
    "Payroll": [r"salary", r"payroll", r"wages"],
    "Marketing": [r"facebook ads", r"google ads", r"ads"],
    "Subscriptions": [r"subscription", r"canva", r"workspace", r"zoom"],
    "Refunds": [r"refund"],
}


def rule_based_category(description: str):
    desc = description.lower()

    for category, patterns in CATEGORY_RULES.items():
        for pattern in patterns:
            if re.search(pattern, desc):
                return {
                    "category": category,
                    "confidence": 0.9,
                    "classified_by": "rules"
                }

    return None
