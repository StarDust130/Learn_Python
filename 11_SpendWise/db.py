
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://stardut:LNRHe9WYRPGe5TcE@cluster0.hfaghq6.mongodb.net/")

db = client["spendwise"]

user_info = db["user"]
money_info = db["money"]
