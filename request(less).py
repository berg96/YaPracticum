import requests

url = 'http://wttr.in/?0T'
response = requests.get(url)
print(response.status_code)

