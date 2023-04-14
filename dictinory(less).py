english = {
    'рука': 'hand',
    'нога': 'leg',
    'хвост': 'tail',
    'питон': 'python',
    'бэкенд-разработчик': 'backend developer'
}

print(english['рука'])
english['рука'] = 'arm'
print(english['рука'])
words_ru = list(english.keys())
words_en = list(english.values())
print(words_ru)
print(words_en)
print(set(english))

favourites_songs_and_ratings = {}

def add_favourite_song(song_name, rank):
    favourites_songs_and_ratings[song_name] = rank

print('Первый вывод на печать: ', favourites_songs_and_ratings)
add_favourite_song('Гражданская Оборона - Моя оборона', 5)
print('Второй вывод на печать: ', favourites_songs_and_ratings)

friends =  {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск'
}

print(friends['Серёга'])
friends['Серёга'] = 'Оренбург'
print('Серёга теперь живёт в славном городе ' + friends['Серёга'])

friends =  {
    'Серёга': 'Оренбург',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}
for city in set(friends.values()):
    print(city)