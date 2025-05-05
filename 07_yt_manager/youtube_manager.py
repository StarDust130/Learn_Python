
import json


def load_data():
     try:
          with open("youtube.txt" , "r") as file:
               return json.load(file)
     except FileNotFoundError:
          return []
     finally:
          print("Chai piyo mera Bhai! 🥰")
     

def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
         json.dump(videos , file)

# (1)
def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index , video in enumerate(videos , start=1):
        print(f"{index}). {video['name']}, Duration: {video['time']} ")

# (2)
def add_video(videos):
   name =  input("Enter Video Name: ")
   time =  input("Enter Video Time: ")

   videos.append({"name": name , "time": time})

   save_data_helper(videos)

# (3)
def update_video(videos):
     pass

# (4)
def delete_video(videos):
     pass

def main ():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = str(input("Enter your choice: "))
        print(f"Videos 📹 {videos}")


        match choice:
            case '1':
                    list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)  
            case "5":
                print("Have a Nice Day! Bye 🍼")
                break
            case _:
                    print("Invalid Choice 😠")
            
            

if __name__ == "__main__":
    main()
