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


import requests

response = requests.get('https://ya.ru/white')

# вот мы узнали, что код ответа 200 и заполучили это число в свой код:
code = response.status_code
print(f'Код ответа = {code}')

# а вот мы и заголовки читаем, и выводим их форматированной строкой
# с примечанием, каким захочется, на любом языке
headers = response.headers
print(f'Тип содержимого: {headers["content-type"]}')
print(f'Время ответа: {headers["date"]}')