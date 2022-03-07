import requests

endpoint = "http://localhost:8000/api/products/1/update/"

data = {"title": "Goodbye, world!"}

get_response = requests.put(endpoint, data)
print(get_response.json())
