import csv
import sqlite3


def create_database():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            description TEXT,
            amount REAL,
            category TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_transaction(date, description, amount, category=""):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO transactions (date, description, amount, category)
        VALUES (?, ?, ?, ?)
    """, (date, description, amount, category))

    conn.commit()
    conn.close()


def insert_from_csv(filename):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM transactions")

    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            date = row[0]
            description = row[1]
            amount = float(row[2])

            cursor.execute("""
                INSERT INTO transactions (date, description, amount, category)
                VALUES (?, ?, ?, ?)
            """, (date, description, amount, ""))

    conn.commit()
    conn.close()
    print("CSV data inserted into database!")


def get_all_transactions():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()

    conn.close()
    return rows


def update_category(transaction_id, category):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE transactions
        SET category = ?
        WHERE id = ?
    """, (category, transaction_id))

    conn.commit()
    conn.close()
    

if __name__ == "__main__":
    create_database()
    insert_from_csv("transactions.csv")

    transactions = get_all_transactions()
    for t in transactions:
        print(t)