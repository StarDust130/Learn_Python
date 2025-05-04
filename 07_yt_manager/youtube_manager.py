

def list_all_videos(videos):
    print("\n")
    print("*" * 70)





while True:
    print("\n Youtube Manager | choose an option ")
    print("1. List all youtube videos ")
    print("2. Add a youtube video ")
    print("3. Update a youtube video details ")
    print("4. Delete a youtube video ")
    print("5. Exit the app ")
    choice = str(input("Enter your choice: "))

    match choice:
        case "1":
            list_all_videos(choice)
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            print("Have a Nice Day! Bye 🍼")
            exit()
