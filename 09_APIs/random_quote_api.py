import requests


def fetch_quotes():
    url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"

    response = requests.get(url)
    data = response.json()

    if data["success"] == True and data.get("data"):
        quote_data = data["data"]

        author = quote_data["author"]
        quote = quote_data["content"]

        return author, quote
    else:
        raise Exception("Fail to fetch user data")
    
    



def main():
    try:
        author, quoute = fetch_quotes()
        print(f"{quoute} - {author}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()        
