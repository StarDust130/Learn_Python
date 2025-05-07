
from pymongo import MongoClient

client = MongoClient(
    "Mongo_URL")

db = client["spendwise"]

user_info = db["user"]
money_info = db["money"]
