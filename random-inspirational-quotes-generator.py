import requests

def get_quote():
    response = requests.get("https://api.quotable.io/random")
    data = response.json()
    return f"{data['content']} - {data['author']}"

if __name__ == "__main__":
    quote = get_quote()
    print(quote)
