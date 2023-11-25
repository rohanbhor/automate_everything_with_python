import requests

query_params = {
    "q": "tesla",
    "from": "2023-10-25",
    "sortBy": "publishedAt",
    "apiKey": "1ece26921ad44472aa0cb633ae023679"
}

url = 'https://newsapi.org/v2/everything'

response = requests.get(url, params=query_params)

print(response.json())