from db import  money_info
import time


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

        # Add income entry
        income_entry = {
            "amount": amount,
            "source": source
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


def add_expense():
    print("💸 Adding income...")


def view_balance():
    print("🧮 Calculating your balance...")


def set_monthly_budget():
    print("📝 Setting your monthly budget...")


def view_financial_report():
    print("📈 Generating report...")

   
