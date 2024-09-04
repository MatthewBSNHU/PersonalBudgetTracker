# summary.py

from income import income_records
from expenses import expense_records

def display_summary():
    """Function to display the summary of income, expenses, and net savings."""
    total_income = sum(record['amount'] for record in income_records)
    total_expenses = sum(record['amount'] for record in expense_records)
    net_savings = total_income - total_expenses

    print("\n--- Monthly Summary ---")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Net Savings: ${net_savings:.2f}")
    print("-----------------------")