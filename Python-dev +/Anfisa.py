def say_about():
    print('Привет, я Анфиса!')
    print('Я персональный помощник.')
    print('Я ещё маленькая,')
    print('но постоянно расту и умнею:')
    print('ведь мой код каждый день дописывают!')

say_about()


temperature = -25
weather = 'солнечно'

print('Сегодня ' + weather)
print(f'Температура воздуха {temperature} градусов')

print('Привет, я Анфиса!')
# допишите код ниже
friends = ['Сергей', 'Соня', 'Дима', 'Алина', 'Егор']

print(friends)


def say_hello(current_hour):
    if current_hour <= 5 or current_hour >= 23:
        print('Доброй ночи!')
    elif current_hour >= 6 and current_hour <= 11:
        print('Доброе утро!')
    elif current_hour >= 12 and current_hour <= 17:
        print('Добрый день!')
    elif current_hour >= 18 and current_hour <= 22:
        print('Добрый вечер!')

say_hello(4)
say_hello(10)
say_hello(15)
say_hello(20)