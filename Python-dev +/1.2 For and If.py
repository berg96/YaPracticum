bremen_musicians = ['Кот', 'Пёс', 'Трубадур', 'Осёл', 'Петух']

for musician in bremen_musicians:
    print(musician)

print('Нам дворцов заманчивые своды не заменят никогда свободы!')

kids = ['Витя', 'Маша', 'Марина']
candies = ['Батончик', 'Сникерс', 'Мишка Косолапый', 'Коровка']

for kid in kids:
    for candy in candies:
        print(kid, 'получает конфету', candy)

for i in range(1, 5):
    print("Вагон №" + str(i))

seasons = ['зима', 'весна', 'лето', 'осень']
for season in reversed(seasons):
    print(season) 

countdown_str = ''

for i in reversed(range(11)):
    countdown_str += str(i) + ', '

countdown_str = countdown_str + 'поехали!'

print(countdown_str)

for messages_count in range(6):
    if messages_count > 0:
        print(f'Новых сообщений: {messages_count}')

for current_hour in range(0, 24):
    print("На часах " + str(current_hour) + ":00.")
    if current_hour < 6:
        print('Доброй ночи!') 
    elif current_hour < 12:
        print('Доброе утро!')
    elif current_hour < 18:
        print('Добрый день!')
    elif current_hour < 23:
        print('Добрый вечер!')
    else:
        print('Доброй ночи!')