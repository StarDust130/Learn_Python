from db import  money_info 
from money_info import add_income, add_expense, view_balance, set_monthly_budget, view_financial_report


def show_Dashboard():
    while True:
        print("\n" + "═" * 45)
        print("💼  Welcome to Your SpendWise Dashboard  💼")
        print("═" * 45)
        print("🔧 Choose an action below:\n")
        print("1️⃣  ➕ Add Income")
        print("2️⃣  ➖ Add Expense")
        print("3️⃣  💰 View Balance")
        print("4️⃣  🎯 Set Monthly Budget")
        print("5️⃣  📊 View Financial Report")
        print("6️⃣  🚪 Logout")
        print("─" * 45)

        choice = input("👉 Enter your choice (1-6): ")

        match choice:
            case "1":
                add_income()
            case "2":
                add_expense()
            case "3":
                view_balance()
            case "4":
                set_monthly_budget()
            case "5":
                view_financial_report()
            case "6":
                print("👋 Logging out... See you soon!")
                break
            case _:
                print("❗ Invalid choice! Please try again.")
