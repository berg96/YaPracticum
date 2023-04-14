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

english = {
    'рука': 'arm',
    'нога': 'leg',
    'хвост': 'tail',
    'питон': 'python',
    'бэкенд-разработчик': 'back-end developer',
    'голова': 'head'
}

new_words = {'мозг': 'brain', 'логика': 'logic'}

english.update(new_words)
print(english)
print(new_words)

friends =  {
    'Серёга': 'Омск', 
    'Соня': 'Москва', 
    'Дима': 'Челябинск'
}
friends['Оля'] = 'Калининград'
friends['Артем'] = 'Мурманск'
print(friends)

favorite_songs = {
    'Тополиный пух': 'Иванушки international',
    'Город золотой': 'Аквариум',
    'Звезда по имени Солнце': 'Кино',
    'Space Oddity': 'David Bowie',
    'Рыба': 'Аквариум',
    'Серенада Трубадура': 'Муслим Магомаев',
}

for singer in favorite_songs.values():
	print('Доктор, я больше не могу слушать исполнителя ' + singer)

for music in favorite_songs.keys():
	print('Доктор, я каждый день по три раза слушаю песню ' + music)
        
friends_names = ['Аня', 'Коля', 'Лёша', 'Лена', 'Миша']
friends_cities = ['Владивосток', 'Красноярск', 'Москва', 'Обнинск', 'Чебоксары']
friends =  {}

for i in range(len(friends_names)):
      friends[friends_names[i]] = friends_cities[i]

print('Лена живёт в городе', friends['Лена'])

friends =  {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Айгуль': 'Казань',	
    'Алёна': 'Белгород',
    'Даниил': 'Санкт-Петербург',
    'Лев': 'Тула',
    'Валера': 'Сыктывкар',
    'Антон': 'Ялта',
    'Карен': 'Краснодар'
}

for friend in friends:
      print(friend, 'живёт в городе', friends[friend])

favorite_songs = {
    'Серёга': ['Unforgiven', 'Holiday', 'Highway to hell'], 
    'Соня': ['Shake it out', 'The Show Must Go On', 'Наше лето'], 
    'Дима': ['Владимирский централ', 'Мурка', 'Третье сентября']
}

print(len(favorite_songs['Серёга']))
for song in favorite_songs['Соня']:
      print(song)

playlist = {
    'Venus',
    'Yesterday',
    'Fireball',
    'Time',
    'Poison',
    'Thunderstruck'
}
new_music = [
    'Kashmir',
    'Smoke on the Water',
    'Bohemian Rhapsody',
    'Zombie',
    'Let It Be',
    'Its My Life',
]

for song in new_music:
      playlist.add(song)
print(playlist)

