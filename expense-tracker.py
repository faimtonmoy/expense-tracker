import argparse
import json
from datetime import datetime


def load_expenses(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def list_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return
    else:
        print(f"{'ID':<4} {'Date':<12} {'Description':<15} {'Amount':<8} ")

        for expense in expenses:
            print(
                f"{expense['id']:<4} {expense['date']:<12} {expense['description']:<15} {expense['amount']:<8.2f}"
            )


def add_expense(expenses, description, amount, file_path="expenses.json"):
    """Add a new expense to the tracker"""
    # Validate amount is positive
    if amount <= 0:
        print(f"Error: Amount must be positive. Got: ${amount}")
        return expenses  # Return unchanged expenses

    new_id = max([exp["id"] for exp in expenses], default=0) + 1
    expense = {
        "id": new_id,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "description": description,
        "amount": amount,
    }
    expenses.append(expense)
    with open(file_path, "w") as file:
        json.dump(expenses, file)
    print(f"Expense added successfully (ID: {new_id})")
    return expenses


def delete_expense(expenses, expense_id, file_path):
    original_length = len(expenses)
    expenses = [exp for exp in expenses if exp["id"] != expense_id]
    if len(expenses) < original_length:
        with open(file_path, "w") as file:
            json.dump(expenses, file)
        print(f"Expense deleted successfully (ID: {expense_id})")
    else:
        print(f"Expense with ID {expense_id} not found.")


def get_summary(expenses, month=None):
    count = 0
    total = 0
    for exp in expenses:
        if month:
            exp_month = datetime.strptime(exp["date"], "%Y-%m-%d").month
            if exp_month == month:
                count += 1
                total += exp["amount"]
            else:
                total += exp["amount"]
                count += 1
        if count < 0:
            if month:
                print(f"No expenses found for month: {month}")
            else:
                print("No expenses found.")
        else:
            if month:
                print(
                    f"Total expenses for month {month}: {total:.2f} ({count} expenses)"
                )
            else:
                print(f"Total expenses: {total:.2f} ({count} expenses)")


def main():
    parser = argparse.ArgumentParser(description="Expense Tracker")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    # add command
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--amount", type=float)
    add_parser.add_argument("--description", required=True)

    # delete command
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--id", type=int, required=True)

    # list command
    list_parser = subparsers.add_parser("list")

    # summary command
    summary_parser = subparsers.add_parser("summary")
    summary_parser.add_argument("--month", type=int)

    args = parser.parse_args()

    expenses = load_expenses("expenses.json")

    if args.command == "add":
        expenses = add_expense(expenses, args.description, args.amount, "expenses.json")
    elif args.command == "delete":
        delete_expense(expenses, args.id, "expenses.json")
    elif args.command == "list":
        list_expenses(expenses)
    elif args.command == "summary":
        get_summary(expenses, month=args.month)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
