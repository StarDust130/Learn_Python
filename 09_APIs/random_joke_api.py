import requests

def fetch_jokes():
    url = 'https://api.freeapi.app/api/v1/public/randomjokes/joke/random'

    responses = requests.get(url)
    data = responses.json()

    if data["success"] and data.get("data"):
        joke_data = data["data"]

        joke = joke_data["content"]

        return joke
    else:
        ("Fail to fetch Jokes! 😆")



def main():
    try:
        joke = fetch_jokes()
        print(f"{joke} 😂")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()