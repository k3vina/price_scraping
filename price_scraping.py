import requests

url = "https://www.jumia.co.ke/"

headers = {
    "User-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
}

response = requests.get(url, headers= headers)
print(response)