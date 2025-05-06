"""
📝 SpendWise – Smart Money Tracker 💸
SpendWise helps you 💰 track your income, 🧾 record expenses, 🎯 set budgets, and 📊 see where your money goes – all from your terminal.

Stay in control of your cash, spend wisely. 😉
"""
import time
from auth import login , create_account
from dashboard import show_Dashboard



def main():
    is_login = False
    while not is_login:
        print("=" * 30)
        print("💸 Welcome to SpendWise 💸")
        print("=" * 30)

        print("1. Login")
        print("2. Create New Account")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        match choice:
            case "1":
                is_login  = login()  # login logic
                if is_login == True:
                    show_Dashboard()
            case "2":
                is_login = create_account()  # login logic
                if is_login == True:
                    show_Dashboard()
            case "3":
                print("Bye 🤭! Have a Nice Day.")
                break
            case _:
                print("\n" * 1)
                print("Invalid Input! 💢😠💢. Try Again")
                time.sleep(2)


if __name__ == "__main__":
    main()
