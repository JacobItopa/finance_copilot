from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

CATEGORIES = [
    "Revenue",
    "Rent",
    "Payroll",
    "Marketing",
    "Subscriptions",
    "Refunds",
    "Utilities",
    "Operations",
    "Uncategorized"
]


def llm_categorize(description: str, context: str):
    prompt = f"""
You are a financial assistant for SMEs.

Recent company transaction history:
{context}

New transaction:
"{description}"

Choose the most appropriate category.
Return ONLY the category.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return {
        "category": response.choices[0].message.content.strip(),
        "confidence": 0.75,
        "classified_by": "llm_rag"
    }

