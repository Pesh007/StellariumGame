import requests

params = {
    "j2000":"[0,0,1]"
}

url = "http://localhost:8090/api/main/view"
response = requests.post(url, params)
print(response)