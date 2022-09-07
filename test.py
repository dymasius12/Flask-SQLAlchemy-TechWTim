import requests 

BASE = "http://127.0.0.1:5000/"

# This means I want to get request from the base + helloworld
# response = requests.get(BASE + "helloworld/tim")
# response = requests.put(BASE + "video/1", {"likes": 10, "name": "Tim", "views": 100000})
# print(response.json())

# input()

response = requests.get(BASE + "video/6")
print(response.json())