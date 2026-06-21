import csv
with open("transactions.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    total = 0
    for row in reader:
        amount = float(row[2])
        total += amount
        print(row[1], amount)
    print("Total: £", total)