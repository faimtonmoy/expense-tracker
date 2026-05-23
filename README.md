# Expense Tracker

A simple command-line expense tracker built with Python. This application allows users to add, list, delete, and summarize expenses while storing data in a local JSON file.

## Project Links

- Project URL: [roadmap.sh Expense Tracker Project](https://roadmap.sh/projects/expense-tracker?utm_source=chatgpt.com)
- GitHub Repository: [Expense Tracker GitHub Repository](https://github.com/faimtonmoy/expense-tracker?utm_source=chatgpt.com)

## Features

- Add new expenses
- Delete existing expenses
- List all expenses
- View total expense summary
- Filter summary by month
- Store expenses in a JSON file

## Technologies Used

- Python
- JSON
- argparse

## Installation

Clone the repository:

```bash
git clone https://github.com/faimtonmoy/expense-tracker.git
```

Navigate to the project directory:

```bash
cd expense-tracker
```

## Usage

### Add an Expense

```bash
$ python expense-tracker.py add --description "Lunch" --amount 20
# Expense added successfully (ID: 1)
```

```bash
$ python expense-tracker.py add --description "Dinner" --amount 10
# Expense added successfully (ID: 2)
```

### List Expenses

```bash
$ python expense-tracker.py list
# ID  Date       Description  Amount
# 1   2024-08-06  Lunch        $20
# 2   2024-08-06  Dinner       $10
```

### View Expense Summary

```bash
$ python expense-tracker.py summary
# Total expenses: $30
```

### Delete an Expense

```bash
$ python expense-tracker.py delete --id 2
# Expense deleted successfully
```

### View Updated Summary

```bash
$ python expense-tracker.py summary
# Total expenses: $20
```

### View Monthly Summary

```bash
$ python expense-tracker.py summary --month 8
# Total expenses for August: $20
```

## File Structure

```plaintext
expense-tracker/
│── expense-tracker.py
│── expenses.json
│── README.md
```

## How It Works

- Expenses are stored in an `expenses.json` file.
- Each expense contains:
  - ID
  - Date
  - Description
  - Amount

## Future Improvements

- Update/edit expenses
- Category support
- CSV export
- Better error handling
- Monthly and yearly reports

## License

This project is open source and available under the MIT License.
