# main.py

from income import add_income, list_income
from expenses import add_expense, list_expenses
from summary import display_summary

def main():
    while True:
        print("\nPersonal Budget Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View All Income")
        print("4. View All Expenses")
        print("5. View Summary")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_income()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            list_income()
        elif choice == '4':
            list_expenses()
        elif choice == '5':
            display_summary()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()