import requests

url = "http://localhost:5000/chat"
data = {"message": "Hello"}
response = requests.post(url, json=data)

print("Bot says:", response.json())
