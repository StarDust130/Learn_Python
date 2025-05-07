
from money_info import add_income, add_expense, view_today_summary, view_financial_report
import time


def show_Dashboard(email, date):
    while True:
        print("\n" + "═" * 45)
        print("💼  Welcome to Your SpendWise Dashboard  💼")
        print("═" * 45)
        print("🔧 Choose an action below:\n")
        print("1️⃣  ➕ Add Income")
        print("2️⃣  ➖ Add Expense")
        print("3️⃣  💰 View Today Summary")
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
                view_today_summary(email, date)
                time.sleep(4)  # Let the user read the summary for 4 seconds

                # Wait for user to press any key
                input("Press any key to return to the dashboard...")
            case "4":
                view_financial_report(email, date)

                time.sleep(4)  # Let the user read the summary for 4 seconds

                # Wait for user to press any key
                input("Press any key to return to the dashboard...")
            case "5":
                print("👋 Logging out... See you soon!")
                break
            case _:
                print("❗ Invalid choice! Please try again.")
