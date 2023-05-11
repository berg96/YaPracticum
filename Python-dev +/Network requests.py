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