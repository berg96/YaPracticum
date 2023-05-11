# Импортируем библиотеку:
import requests

# Отправляем GET-запрос:
response = requests.get('http://info.cern.ch/')

print(response.text)  # Печатаем код запрошенной страницы.


import requests

url = 'http://wttr.in/?0T'

response = requests.get(url)  # Выполните HTTP-запрос.

print(response.status_code)  # Напечатайте статус-код ответа.
print(response.text)


import requests

search_parameters = {
    'text': 'что такое backend',
    'lr': 213
}
url = 'https://yandex.ru/search/'
# Функция get() приняла на вход URL и параметры поиска,
# а дальше она знает, что делать
response = requests.get(url, params=search_parameters)

print(response.status_code)
print(response.url)