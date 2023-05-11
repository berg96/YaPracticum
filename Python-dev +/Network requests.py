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
#print(f'Время ответа: {headers["date"]}')


import requests

url = 'https://wttr.in'

weather_parameters = {
    '0': '',
    'T': '',
    'M': '',
}

request_headers = {
    'Accept-Language': 'ru'
    # заполните словарь с заголовками
}

# не забудьте передать параметры и заголовки в http-запрос
# через аргументы `params` и `headers` функции get()
response = requests.get(url, params = weather_parameters, headers = request_headers)
print(response.text)


import requests


cities = [
    'Омск',
    'Калининград',
    'Челябинск',
    'Владивосток',
    'Красноярск',
    'Москва',
    'Екатеринбург'
]


def make_url(city):
    # в URL задаём город, в котором узнаем погоду
    return f'http://wttr.in/{city}'


def make_parameters():
    params = {
        'format': 2,  # погода одной строкой
        'M': ''  # скорость ветра в "м/с"
    }
    return params


def what_weather(city):
    try:
        response = requests.get(make_url(city),params=make_parameters())
    except requests.ConnectionError:
        return '<сетевая ошибка>'
    if response.status_code == 200:
        return response.text
    else:
        return '<ошибка на сервере погоды>'
    # Напишите тело этой функции.
    # Не изменяйте остальной код!

print('Погода в городах:')
for city in cities:
    print(city, what_weather(city))
