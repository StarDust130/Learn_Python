# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

weather = str(input("Enter Weather: ").lower().strip())

activity_dic = {
    "sunny": "Go for a walk",
    "rainy": "Read a book",
    "snowy": "Build a snowman"
}

activity = activity_dic.get(weather , "Opps! Not Found")

if weather in activity_dic:
    print(f"Best Activity for you is: {activity_dic[weather]}")
else:
    print(
        f"Oops! Not Found. Try one of these: {', '.join(activity_dic.keys())}")




