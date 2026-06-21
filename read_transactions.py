import csv

def load_transactions(filename):
    transactions = []

    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            amount = float(row[2])
            transactions.append({
                "date": row[0],
                "description": row[1],
                "amount": amount
            })

    return transactions


transactions = load_transactions("transactions.csv")

for t in transactions:
    print(t)

total = sum(t["amount"] for t in transactions)
print(f"Total: £{total:.2f}")