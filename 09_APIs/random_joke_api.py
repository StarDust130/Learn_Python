import requests


def fetch_jokes():
    url = 'https://api.freeapi.app/api/v1/public/randomjokes/joke/random'

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data["success"] and data.get("data"):
            joke_data = data["data"]
            return joke_data.get("content", "No joke found!")
        else:
            return "Failed to fetch joke! 😆"

    except Exception as e:
        return f"Error fetching joke: {str(e)}"


def main():
    joke = fetch_jokes()
    print(f"{joke} 😂")


if __name__ == "__main__":
    main()
