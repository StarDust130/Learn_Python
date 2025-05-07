
from money_info import add_income, add_expense, view_balance, view_financial_report


def show_Dashboard(email, date):
    while True:
        print("\n" + "═" * 45)
        print("💼  Welcome to Your SpendWise Dashboard  💼")
        print("═" * 45)
        print("🔧 Choose an action below:\n")
        print("1️⃣  ➕ Add Income")
        print("2️⃣  ➖ Add Expense")
        print("3️⃣  💰 View Balance")
        print("4️⃣  📊 View Financial Report")
        print("5️⃣  🚪 Logout")
        print("─" * 45)

        choice = input("👉 Enter your choice (1-5): ")

        match choice:
            case "1":
                add_income(email, date)
            case "2":
                add_expense(email, date)
            case "3":
                view_balance(email, date)
            case "4":
                view_financial_report(email, date)
            case "5":
                print("👋 Logging out... See you soon!")
                break
            case _:
                print("❗ Invalid choice! Please try again.")
