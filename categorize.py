import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

def categorize_transaction(description, amount):
    if amount < 0:
        transaction_type = "an expense (money spent)"
    else:
        transaction_type = "income (money received)"

    prompt = f"""Categorize this transaction into ONE word.
Description: {description}
Amount: £{amount} ({transaction_type})

Common categories: Groceries, Income, Subscriptions, Transport, Entertainment, Bills, Shopping, Dining, Other.

Reply with just one word."""

    response = model.generate_content(prompt)
    return response.text.strip()


if __name__ == "__main__":
    category = categorize_transaction("Tesco", -45.20)
    print(category)