user_query = 'как стать бэкенд-разработчиком'

url = 'https://yandex.ru/search/?text=' +  '%20'.join(user_query.split())

print(url)


import urllib.parse

strings = [
    'Что такое backend',
    'Привет!',
    ' ',        # Просто пробел.
    'letiště',  # Аэропорт по-чешски.
    'München',  # Крупнейший город Баварии.
    'Champs-Élysées',  # Елисейские поля.
    '東京',     # А это Токио.
]

for s in strings:
    encoded = urllib.parse.quote(s)          # Зашифрованная строка.
    decoded = urllib.parse.unquote(encoded)  # Расшифрованная обратно строка.
    print(decoded, '-', encoded)