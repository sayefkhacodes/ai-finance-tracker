import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

def categorize_transaction(description, amount):
    prompt = f"Categorize this transaction: {description}, £{amount}. Reply with just one word for the category."
    response = model.generate_content(prompt)
    return response.text.strip()


if __name__ == "__main__":
    category = categorize_transaction("Tesco", -45.20)
    print(category)