# income.py

income_records = []  # List to store all income records

def add_income():
    """Function to add an income record to the list."""
    try:
        source = input("Enter the source of income (e.g., Salary, Freelance): ")
        amount = float(input("Enter the amount: $"))
        date = input("Enter the date (e.g., YYYY-MM-DD): ")
        
        # Append the new income record as a dictionary to the list
        income_records.append({'source': source, 'amount': amount, 'date': date})
        print("Income added successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

def list_income():
    """Function to list all income records."""
    if income_records:
        print("\nIncome Records:")
        for record in income_records:
            print(f"Source: {record['source']}, Amount: ${record['amount']:.2f}, Date: {record['date']}")
    else:
        print("No income records found.")