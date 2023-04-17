import requests

url = 'http://wttr.in/?0T'
response = requests.get(url)
print(response.status_code)
#print(response.text)

url = 'https://wttr.in'

weather_parameters = {
    '0': '',
    'T': '1'
}

response = requests.get(url, params=weather_parameters)  # передайте параметры в http-запрос

print(response.text)