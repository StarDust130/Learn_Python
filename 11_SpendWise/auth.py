
from db import user_info, money_info
import time


from datetime import datetime


def login():
    print("\n" + "-" * 10)
    print("💻  Login to SpendWise Terminal  💻")
    print("🔓" * 10 + "\n")

    email = input("🧑‍💼 Email ID: ")
    password = input("🕵️ Password: ")

    user = user_info.find_one({"email": email, "password": password})

    if user:
        today = datetime.today().strftime("%Y-%m-%d")

        print(today)

        # Check if today's doc already exists
        existing_doc = money_info.find_one({"email": email, "date": today})

        if not existing_doc:
            money_info.insert_one({
                "email": email,
                "date": today,
                "income": [],
                "expenses": [],
            })

        print("\n✅ Access Granted! Welcome back, Commander 🧠\n")
        time.sleep(2)
        return True

    else:
        print("\n❌ Access Denied! Invalid credentials ⚠️\n")
        return False

def create_account():
    print("\n" + "🎉" * 10)
    print("✨ Create Your Account ✨")
    print("🎉" * 10 + "\n")

    email = input("📧 Enter Email: ")
    password = input("🔐 Enter Password: ")

    user_info.insert_one({"email": email, "password": password})

    print("\n✅ Account created successfully! Login Please 🚀\n")

    return True
