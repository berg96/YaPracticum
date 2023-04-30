unique_songs = {
    'Рок-колыбельная',
    'Ничего на свете лучше нету',
    'Мы к вам заехали на час',
    'А как известно, мы народ горячий',
    'Луч Солнца Золотого',
    'Куда ты, тропинка, меня завела'
}
print('Только один концерт! Проездом из Бремена в Рио-де-Жанейро!')
print('БРЕМЕНСКИЕ МУЗЫКАНТЫ!')

for song in unique_songs:
    print(song)

print('Не опаздывайте, начало в 19:00')

cities = [
    'Вологда',
    'Чебоксары',
    'Тольятти',
    'Москва',
    'Бремен',
    'Санкт-Петербург',
    'Новороссийск',
    'Челябинск',
    'Вологда',
    'Новосибирск',
    'Челябинск',
    'Санкт-Петербург',
    'Москва',
    'Новосибирск'
]

unique_cities = set(cities)
for city in unique_cities:
    print('-',city)

playlist = {
    'Venus',
    'Yesterday',
    'Fireball',
    'Time',
    'Poison'
}

playlist.add('Thunderstruck')
print(playlist)

playlist_1 = {'Три белых коня', 'Happy new year', 'Снежинка'}
playlist_2 = {'Last christmas', 'Снежинка', 'Happy new year'}
playlist_3 = playlist_1.union(playlist_2)
print(playlist_3)

playlist_4 = playlist_1.difference(playlist_2)
print(playlist_4)

playlist_5=playlist_1.intersection(playlist_2)
print(playlist_5)

def print_valid_cities(all_cities,used_cities):
    valid_cities=all_cities.difference(used_cities)
    for city in valid_cities:
        print(city)

def add_cities(all_cities, new_cities):
    # Напишите код функции
    for city in new_cities:
        all_cities.add(city)

new_cities = [
    'Екатеринбург',
    'Выборг' ,
    'Владивосток',
    'Казань',
    'Why',
    'Йезд'
]

all_cities = {
    'Абакан',
    'Астрахань', 
    'Бобруйск', 
    'Калуга',
    'Караганда',
    'Кострома',
    'Липецк', 
    'Новосибирск'
}

used_cities = {'Калуга', 'Абакан' , 'Новосибирск'}

add_cities(all_cities, new_cities)
print_valid_cities(all_cities, used_cities)

def get_together_games(games_1,games_2):
    return set(games_1).intersection(set(games_2))

anfisa_games = [
    'Online-chess',
    'Города',
    'DOOM',
    'Крестики-нолики'
]
alisa_games = [
    'DOOM',
    'Online-chess',
    'Города',
    'GTA',
    'World of tanks'
]

for game in get_together_games(anfisa_games,alisa_games):
    print('👾',game)
