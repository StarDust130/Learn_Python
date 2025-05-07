from db import  money_info
import time
from datetime import datetime
from helper import format_date


def add_income(email, date):
    print("\n" + "💰" * 10)
    print("💸  Add New Income Entry")
    print("💰" * 10 + "\n")

    try:
        amount_input = input("📝 Enter Income Amount (₹): ").strip()
        amount = float(amount_input)

        if amount <= 0:
            print("\n🚫 Amount must be greater than zero. Try again.\n")
            return

        source = input(
            "🏷️  Income Source (e.g., 💼 Salary, 🛠️ Freelance): ").strip()
        if not source:
            source = "❓ Unknown"

        # Add income entry in DB 🐼
        income_entry = {
            "amount": amount,
            "source": source,
            "time": datetime.now().strftime("%H:%M:%S")
        }

        money_info.update_one(
            {"email": email, "date": date},
            {"$push": {"income": income_entry}}
            
        )

        

        print(f"\n✅ Successfully added ₹{amount:.2f} from '{source}' 🧾\n")

        time.sleep(3)

    except ValueError:
        print("\n❌ Invalid input. Please enter a valid number for income.\n")

    except Exception as e:
        print(f"\n⚠️ Unexpected error: {e}\n")


def add_expense(email, date):
    print("\n" + "🧾" * 12)
    print("💸  Add an Expense to Your Tracker")
    print("🧾" * 12 + "\n")

    try:
        amount_input = input("💰 Amount Spent (₹): ")
        amount = float(amount_input)

        if amount <= 0:
            print("\n🚫 Amount must be more than ₹0. Try again!\n")
            return

        category = input(
            "📌 What did you spend on? (e.g., 🍔 Food, 🚕 Travel): ").strip()
        if not category:
            category = "❓ Unknown"

        expense_entry = {
            "amount": amount,
            "source": category,
            "time": datetime.now().strftime("%H:%M:%S")
        }

        money_info.update_one(
            {"email": email, "date": date},
            {"$push": {"expenses": expense_entry}}
        )

        print(f"\n✅ Logged ₹{amount:.2f} for '{category}' 🧾\n")
        time.sleep(1.5)

    except ValueError:
        print("\n❌ Oops! That wasn't a valid number.\n")

    except Exception as e:
        print(f"\n⚠️ Error occurred: {e}\n")


def view_today_summary(email, date):
    print("\n" + "📊" * 10)
    print(f"📅 Daily Summary for {format_date(date)}")
    print("📊" * 10 + "\n")

    # Fetch today's document from the database
    today_info = money_info.find_one({"email": email, "date": date})

    if not today_info:
        print("❗ No records found for today. Add some income or expenses first!\n")
        return

    # Calculate total income and expenses
    total_income = sum(entry["amount"] for entry in today_info.get("income", []))
    total_expenses = sum(entry["amount"] for entry in today_info.get("expenses", []))

    # Show the summary
    print(f"💰 Total Income: ₹{total_income:.2f}")
    print(f"💸 Total Expenses: ₹{total_expenses:.2f}")
    print(f"🧾 Net Balance: ₹{total_income - total_expenses:.2f}")

    # Optional: Show the largest expense of the day
    top_expenses = sorted(today_info.get("expenses", []), key=lambda x: x["amount"], reverse=True)
    if top_expenses:
        top_expense = top_expenses[0]
        print(f"\n🔍 Top Expense: {top_expense['source']} - ₹{top_expense['amount']:.2f}")

    print("\n" + "📊" * 10)

    

