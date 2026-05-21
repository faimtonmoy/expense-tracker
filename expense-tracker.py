import argparse
import json


def load_expenses(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def main():
    parser = argparse.ArgumentParser(description="Expense Tracker")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    # add command
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("amount", type=float)
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
        print(f"Adding expense: {args.amount} - {args.description}")
    elif args.command == "delete":
        print(f"Deleting expense with ID: {args.id}")
    elif args.command == "list":
        print("Listing all expenses")
    elif args.command == "summary":
        print(f"Showing summary for month: {args.month}")


if __name__ == "__main__":
    main()
