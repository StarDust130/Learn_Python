"""
📝 SpendWise – Smart Money Tracker 💸
SpendWise helps you 💰 track your income, 🧾 record expenses, 🎯 set budgets, and 📊 see where your money goes – all from your terminal.

Stay in control of your cash, spend wisely. 😉
"""
from pymongo import MongoClient
import time

client = MongoClient(
    "Mongo_URL")

db = client["spendwise"]

user_info = db["user"]
money_info = db["money"]


def login():
    print("\n" + "-" * 10)
    print("💻  Login to SpendWise Terminal  💻")
    print("🔓" * 10 + "\n")

    email = input("🧑‍💼 Email ID: ")
    password = input("🕵️ Password: ")

    user = user_info.find_one({"email": email, "password": password})

    if user:
        print("\n✅ Access Granted! Welcome back, Commander 🧠\n")
    else:
        print("\n❌ Access Denied! Invalid credentials ⚠️\n")



def create_account():
    print("\n" + "🎉" * 10)
    print("✨ Create Your Account ✨")
    print("🎉" * 10 + "\n")

    email = input("📧 Enter Email: ")
    password = input("🔐 Enter Password: ")

    user_info.insert_one({"email": email, "password": password})

    print("\n✅ Account created successfully! Welcome aboard 🚀\n")



def main():
    while True:
        print("=" * 30)
        print("💸 Welcome to SpendWise 💸")
        print("=" * 30)

        print("1. Login")
        print("2. Create New Account")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        match choice:
            case "1":
                login()  # login logic
            case "2":
                create_account()  # create account logic
            case "3":
                print("Bye 🤭! Have a Nice Day.")
                break
            case _:
                print("\n" * 1)
                print("Invalid Input! 💢😠💢. Try Again")
                time.sleep(2)


if __name__ == "__main__":
    main()
