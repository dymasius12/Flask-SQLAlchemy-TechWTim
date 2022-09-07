import requests 

BASE = "http://127.0.0.1:5000/"

# This means I want to get request from the base + helloworld
# response = requests.get(BASE + "helloworld/tim")

# data = [{"likes": 78, "name": "Joe", "views": 100000},
#         {"likes": 2000000, "name": "How to make REST API", "views": 500000000},
#         {"likes": 35, "name": "Tim", "views": 100000}]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())

# # input()
# # response = requests.delete(BASE + "video/0")
# # print(response)
# input()

response = requests.get(BASE + "video/2", {"views":99})
print(response.json())