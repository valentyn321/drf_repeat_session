import requests

endpoint = "http://localhost:8000/api/products/8/"


get_response = requests.get(
    endpoint, params={"abc": 123}, json={"content": "Hello, world!"}
)
print(get_response.json())
