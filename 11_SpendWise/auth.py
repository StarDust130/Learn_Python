
from db import user_info
import time


def login():
    print("\n" + "-" * 10)
    print("💻  Login to SpendWise Terminal  💻")
    print("🔓" * 10 + "\n")

    email = input("🧑‍💼 Email ID: ")
    password = input("🕵️ Password: ")

    user = user_info.find_one({"email": email, "password": password})

    if user:
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
