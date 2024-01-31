import requests

def postear(json):
    url = "http://127.0.0.1:8000/"
    response = requests.post(url, data=json)
    response
    print(response.text)
