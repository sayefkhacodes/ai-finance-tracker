from database import get_all_transactions


def get_summary():
    transactions = get_all_transactions()

    total_income = 0
    total_expenses = 0
    by_category = {}

    for t in transactions:
        amount = t[3]
        category = t[4]

        if amount > 0:
            total_income += amount
        else:
            total_expenses += amount

        if category not in by_category:
            by_category[category] = 0
        by_category[category] += amount

    return {
        "total_income": total_income,
        "total_expenses": total_expenses,
        "net": total_income + total_expenses,
        "by_category": by_category
    }


if __name__ == "__main__":
    summary = get_summary()

    print(f"Total income: £{summary['total_income']:.2f}")
    print(f"Total expenses: £{summary['total_expenses']:.2f}")
    print(f"Net: £{summary['net']:.2f}")
    print()
    print("By category:")
    for category, amount in summary["by_category"].items():
        print(f"  {category}: £{amount:.2f}")