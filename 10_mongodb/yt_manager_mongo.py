#

from pymongo import MongoClient

client = MongoClient(
    "Mongo_URL")

db = client["ytmanager"]

video_collection = db["videos"]


def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']} , Name: {video['name']} and Time {video['time']} ")


def add_videos():
    name = input("Enter Video Name: ")
    time = input("Enter Video Time: ")

    video_collection.insert_one({"name": name, "time": time})


def update_videos():
    name = input("Enter Video Name: ")
    time = input("Enter Video Time: ")
    id = input("Enter Video Id: ")

    video_collection.update_one(
        {"_id": id},
        {"$set" : 
        {"name": name} , "time": time})


def delete_videos():
    id = int(input("Enter the video number to delete ❌: "))

    video_collection.delete_one({"_id": id})


def main():
    while True:
        print("\n Youtube manger app with DB. 😚")
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")

        choice = str(input("Enter your choice: "))

        if choice == "1":
            list_videos()
        elif choice == "2":
            add_videos()
        elif choice == "3":
            update_videos()
        elif choice == "4":
            delete_videos()
        elif choice == "5":
            break
        else:
            print("Invalid Choice 😠")

    client.close()


if __name__ == "__main__":
    main()
