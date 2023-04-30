import requests

url = 'http://wttr.in/?0T'
response = requests.get(url)
print(response.status_code)
#print(response.text)

url = 'https://wttr.in'

weather_parameters = {
    '0': '',
    'T': '1',
    'M': '',
}

request_headers = {
    'Accept-Language': 'ru'
}

response = requests.get(url, params=weather_parameters, headers=request_headers)  # передайте параметры в http-запрос
headers = response.headers

print(response.text)
print(f'Время ответа: {headers["date"]}') 

