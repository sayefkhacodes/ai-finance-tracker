import matplotlib.pyplot as plt
from summary import get_summary

summary = get_summary()
expenses = {k: abs(v) for k, v in summary["by_category"].items() if v < 0}

categories = list(expenses.keys())
amounts = list(expenses.values())

plt.figure(figsize=(8, 6))
plt.pie(amounts, labels=categories, autopct="%1.1f%%")
plt.title("Spending by Category")
plt.savefig("spending_chart.png")
print("Chart saved as spending_chart.png")