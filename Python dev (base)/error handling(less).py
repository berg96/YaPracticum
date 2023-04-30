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
    return f'http://wttr.in/{city}'


def make_parameters():
    params = {
        'format': 2,
        'M': ''
    }
    return params


def what_weather(city):
    try:
        response = requests.get(url=make_url(city), params=make_parameters())
        if response.status_code == 200:
            return response.text
        else:
            return '<ошибка на сервере погоды>'
    except requests.ConnectionError:
        return '<сетевая ошибка>'

print('Погода в городах:')
for city in cities:
    print(city, what_weather(city))
