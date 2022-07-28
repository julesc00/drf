import requests


URL = "http://127.0.0.1:8000/"
ENDPOINT = "https://httpbin.org/status/200/"
ENDPOINT2 = "https://httpbin.org/status/anything"

response = requests.get(URL, json={"query": "Hello World"}).text
print(response)
