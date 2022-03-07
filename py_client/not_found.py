import requests

endpoint = "http://localhost:8000/api/products/8796541641/"


get_response = requests.get(
    endpoint,
)
print(get_response.json())
