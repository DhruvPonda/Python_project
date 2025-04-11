import pandas as pd
from datetime import datetime

# Initialize the transactions data
transactions = pd.DataFrame(columns=["Type", "Amount", "Description", "Date"])

# Load existing transactions from CSV file
try:
    transactions = pd.read_csv("transactions.csv")
except FileNotFoundError:
    pass

def add_transaction(trans_type, amount, description):
    global transactions
    date = datetime.now().strftime("%Y-%m-%d")
    new_transaction = pd.DataFrame([[trans_type, amount, description, date]], columns=["Type", "Amount", "Description", "Date"])
    transactions = pd.concat([transactions, new_transaction], ignore_index=True)
    transactions.to_csv("transactions.csv", index=False)
    print("\nTransaction added successfully!\n")

def view_transactions():
    global transactions
    print("\nTransaction History:")
    if transactions.empty:
        print("No transactions found.")
    else:
        print(transactions[["Type", "Amount", "Description"]])
    print()

def generate_summary(period):
    global transactions
    start_date, end_date = period.split(":")
    filtered_transactions = transactions[(transactions["Date"] >= start_date) & (transactions["Date"] <= end_date)]
    total_income = filtered_transactions[filtered_transactions["Type"] == "income"]["Amount"].sum()
    total_expenses = filtered_transactions[filtered_transactions["Type"] == "expense"]["Amount"].sum()
    net_savings = total_income - total_expenses
    
    print("\nFinancial Summary:")
    print(f"Total Income: ${total_income}")
    print(f"Total Expenses: ${total_expenses}")
    print(f"Net Savings: ${net_savings}\n")

def main():
    while True:
        print("Welcome to the Personal Finance Tracker!")
        print("Please choose an option:")
        print("1. Add a new transaction")
        print("2. View transaction history")
        print("3. Generate financial summary")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            trans_type = input("Enter transaction type (income/expense): ").strip().lower()
            amount = float(input("Enter amount: "))
            description = input("Enter description: ").strip()
            add_transaction(trans_type, amount, description)
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            period = input("Enter the period for summary (e.g., '2025-03-01:2025-03-31'): ").strip()
            generate_summary(period)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()