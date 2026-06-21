from database import get_all_transactions, update_category
from categorize import categorize_transaction

transactions = get_all_transactions()

for t in transactions:
    transaction_id = t[0]
    description = t[2]
    amount = t[3]
    existing_category = t[4]

    if existing_category:
        print(f"Skipping {description}, already categorized as {existing_category}")
        continue

    category = categorize_transaction(description, amount)
    print(f"{description}: {category}")

    update_category(transaction_id, category)