# PersonalBudgetTracker

Features
Add Income: Record different sources of income.
Add Expense: Record various types of expenses.
View All Income: List all recorded income entries.
View All Expenses: List all recorded expense entries.
View Summary: See a summary of total income, total expenses, and net savings.

Usage
Run the Application:

bash
Copy code
python main.py
Follow the On-Screen Menu:

1: Add Income
2: Add Expense
3: View All Income
4: View All Expenses
5: View Summary
6: Exit

File Structure
main.py: Entry point of the application.
income.py: Contains functions for managing income records.
expenses.py: Contains functions for managing expense records.
summary.py: Contains functions for generating financial summaries.
Example
Here’s a sample interaction with the application:


Personal Budget Tracker
1. Add Income
2. Add Expense
3. View All Income
4. View All Expenses
5. View Summary
6. Exit

Enter your choice: 1
Enter the source of income (e.g., Salary, Freelance): Salary
Enter the amount: $5000
Enter the date (e.g., YYYY-MM-DD): 2024-09-01
Income added successfully!

Enter your choice: 5
--- Monthly Summary ---
Total Income: $5000.00
Total Expenses: $0.00
Net Savings: $5000.00

