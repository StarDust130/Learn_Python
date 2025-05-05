import sqlite3

conn = sqlite3.connect("yt_manager.db")

cursor = conn.cursor()

cursor.execute("""
     CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
               )
 """)


def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)


def add_videos():
    name = input("Enter Video Name: ")
    time = input("Enter Video Time: ")

    cursor.execute(
        "INSERT INTO videos (name , time) VALUES (?,?)", (name, time))

    conn.commit()


def update_videos():
    name = input("Enter Video Name: ")
    time = input("Enter Video Time: ")
    id = input("Enter Video Id: ")

    cursor.execute(
        "UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, id))

    conn.commit()


def delete_videos():
    id = int(input("Enter the video number to delete ❌: "))

    cursor.execute("DELETE FROM videos where id = ?", (id,))

    conn.commit()


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

    conn.close()


if __name__ == "__main__":
    main()
