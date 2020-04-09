import requests

url = "http://google.com"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response)
print(response.status_code)
# print(response.text)
print(response.ok)
# print(response.text.encode("utf8"))
