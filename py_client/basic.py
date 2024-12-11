import requests

endpoint = 'http://localhost:8000/api/products/'
# endpoint = 'http://localhost:8000/api/products/1/'

# response = requests.post(endpoint, json=({"title": "good morning", "content": "continued with drf this morning", "price": 100.00}))
# print(response.text)
# print(response.status_code)
response = requests.get(endpoint)
print(response.json())