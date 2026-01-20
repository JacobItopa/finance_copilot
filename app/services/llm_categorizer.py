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


def llm_categorize(description: str):
    prompt = f"""
You are a financial assistant for SMEs.

Transaction description:
"{description}"

Choose the most appropriate category from this list:
{", ".join(CATEGORIES)}

Return ONLY the category name.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    category = response.choices[0].message.content.strip()

    return {
        "category": category,
        "confidence": 0.7,
        "classified_by": "llm"
    }
