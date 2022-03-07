import requests

endpoint = "http://localhost:8000/api/products/"


get_response = requests.post(endpoint, {"title": "Title is equal to content"})
print(get_response.json())
