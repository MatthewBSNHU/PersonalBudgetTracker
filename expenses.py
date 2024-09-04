# expenses.py

expense_records = []  # List to store all expense records

def add_expense():
    """Function to add an expense record to the list."""
    try:
        category = input("Enter the category of expense (e.g., Groceries, Rent): ")
        amount = float(input("Enter the amount: $"))
        date = input("Enter the date (e.g., YYYY-MM-DD): ")
        
        # Append the new expense record as a dictionary to the list
        expense_records.append({'category': category, 'amount': amount, 'date': date})
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

def list_expenses():
    """Function to list all expense records."""
    if expense_records:
        print("\nExpense Records:")
        for record in expense_records:
            print(f"Category: {record['category']}, Amount: ${record['amount']:.2f}, Date: {record['date']}")
    else:
       print("No expense records were found ")