import requests
import json

######################################
#LIST
######################################
url = "https://reqres.in/api/users"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
data = json.loads(response.text)
users_data = data.get('data')

print(users_data)

######################################
#CREATE
######################################
url = "https://reqres.in/api/users?name=Ignacio&job=profesor"

payload={}
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)
created_user = response.text
print(created_user)

######################################
#UPDATE
######################################
url = "https://reqres.in/api/users/2?name=morpheus&residence=zion"

payload={}
headers = {}

response = requests.request("PUT", url, headers=headers, data=payload)
updated_user = response.text
print(updated_user)

######################################
#DELETE
######################################
url = "https://reqres.in/api/users/2?name=Tracey"

payload={}
headers = {}

response = requests.request("DELETE", url, headers=headers, data=payload)
print(response)