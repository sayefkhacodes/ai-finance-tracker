import csv
with open("transactions.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)