songs_list = [
    'Мы к вам заехали на час',
    'А как известно, мы народ горячий',
    'Куда ты, тропинка, меня завела',
    'Луч Солнца Золотого',
    'Рок-колыбельная',
    'Рок-колыбельная',
    'Куда ты, тропинка, меня завела',
    'А как известно, мы народ горячий',
    'Луч Солнца Золотого',
    'Ничего на свете лучше нету',
    'А как известно, мы народ горячий',
    'Луч Солнца Золотого',
    'Мы к вам заехали на час',
    'Ничего на свете лучше нету',
    'Куда ты, тропинка, меня завела',
    'Луч Солнца Золотого'
]

unique_songs = set(songs_list)

print(unique_songs)

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
    print(f'- {city}')


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


playlist_1 = {'Голубой вагон', 'Облака', 'Yesterday', 'Наше лето'}
playlist_2 = {'Наше лето', 'Голубой вагон', 'Облака'}
playlist_3 = playlist_1.difference(playlist_2)

print(playlist_3)


films_1 = {'Форсаж', 'Достучаться до небес', 'Мстители: война бесконечности'}
films_2 = {'Мстители: война бесконечности', 'Форсаж', 'Матрица'}
films_3 = films_1.intersection(films_2)

print(films_3)


def print_valid_cities(all_cities,used_cities):
    for city in all_cities.difference(used_cities):
        print(city)

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

print_valid_cities(all_cities, used_cities)


english = {
    'рука': 'hand', # Первый элемент словаря (да, в каждом элементе две части!)
    'нога': 'leg',  # Второй элемент словаря
    'хвост': 'tail',  # Третий элемент
    'питон': 'python',  # Четвёртый элемент
    'бэкенд-разработчик': 'back-end developer'  # Пятый элемент
} 

print(english['рука'])


dump = {
    1: 'единица',               # Ключ - число, значение - строка.
    'земляника': 'ягода',       # И ключ, и значение - строки.
    'помидор': 'ягода',         # Значение 'ягода' - не уникально. Так можно.
    False: 0,                   # Ключ - булево значение, значение - число.
    'лук': ['овощ', 'оружие'],  # Ключ - строка, значение - список.
    # Ключ - строка, а значение - словарь. Так тоже можно!
    'англо-русский словарь': {'рука': 'hand', 
                              'нога': 'leg', 
                              'бэкенд-разработчик': 'back-end developer'
                               },    
}

print(dump['лук'])


english = {
    'рука': 'hand',
	'нога': 'leg',
    'хвост': 'tail',
    'питон': 'python',
	'бэкенд-разработчик': 'backend developer'
}

# Элементу с ключом 'рука' присвоим новое значение:
english['рука'] = 'arm'

print(english['рука'])


old_letters = {
    'ять': 'Ѣ',
    'юс малый': 'Ѧ',
    'юс большой': 'Ѫ'}

print(old_letters.values())


favorite_songs = {
    'Тополиный пух': 'Иванушки international',
    'Город золотой': 'Аквариум',
    'Звезда по имени Солнце': 'Кино'
}

print(favorite_songs.keys())


favourites_songs_and_ratings = {}

def add_favourite_song(song_name, rank):
    favourites_songs_and_ratings[song_name] = rank

# Словарь пока что пуст:
print('Первый вывод на печать: ', favourites_songs_and_ratings)

add_favourite_song('Гражданская Оборона - Моя оборона', 5)

# А здесь словарь уже обновлен и не пуст:
print('Второй вывод на печать: ', favourites_songs_and_ratings)


english = {
    'рука': 'arm',
    'нога': 'leg',
    'хвост': 'tail',
    'питон': 'python',
    'бэкенд-разработчик': 'back-end developer',
    'голова': 'head'
}

# Объявим новый словарь
new_words = {'мозг': 'brain', 'логика': 'logic'}

# Добавим в словарь english элементы словаря new_words
english.update(new_words)

# Посмотрим, что теперь хранится в словаре english
print(english)

# Заодно выясним, что произошло со словарём new_words
print(new_words)


favorite_songs = {
    'Тополиный пух': 'Иванушки international',
    'Город золотой': 'Аквариум',
    'Звезда по имени Солнце': 'Кино',
    'Space Oddity': 'David Bowie',
    'Рыба': 'Аквариум',
    'Серенада Трубадура': 'Муслим Магомаев',
}

for song, performer in favorite_songs.items():
	print('Песню ' + song + ' исполняет ' + performer)
        

# Список (list): в квадратных скобках:
sleep_list = [
    'спать', 
    'дрыхнуть', 
    'кемарить',
    'спать'
] 

# Множество (set): в фигурных скобках, элементы выглядят как в списке,
# но не могут повторяться:
sleep_set = {
    'дрыхнуть', 
    'спать', 
    'кемарить'
} 
# Словарь (dict): в фигурных скобках, элементы выглядят как ключ:значение;
# ключи не могут повторяться:
sleep_dict = {
    'спать': 'дрыхнуть', 
    'почивать': 'кемарить'
}

# Есть ли элемент 'дрыхнуть' в списке sleep_list?
if 'дрыхнуть' in sleep_list:
    print('В списке: нашлось!') 
else:
    print('В списке: не нашлось :(')

# Есть ли элемент 'дрыхнуть' в сете sleep_set?
if 'дрыхнуть' in sleep_set:
    print('В сете: нашлось!') 
else:
    print('В сете: не нашлось :(')

# Есть ли элемент 'дрыхнуть' в словаре sleep_dict?
if 'дрыхнуть' in sleep_dict:
    print('В словаре: нашлось!') 
else:
    print('В словаре: не нашлось :(')


sleep_list = [
    'спать', 
    'дрыхнуть', 
    'кемарить', 
    'спать'
] 
# Метод append() добавит строку 'посапывать' в конец списка
sleep_list.append('посапывать')
print(sleep_list)


mobile_devices = {
    'cucuPhone': 2010,
    'cucuBlet': 2013,
    'cucuClock': 2015,
    'cucuEar': 2018,
    'cuCube': 2015,
}

home_devices = {
    'cucuLot': 2011,
    'cucuBlock': 2010,
    'cucuWall': 2010,
    'cucuMonitor': 2020,
    'cucuLamp': 2015,
    'cucuTable': 2016,
    'cucuTV': 2017,
}

not_supported_devices = {'cucuBlock', 'cucuBlet', 'cucuWall'}

result_catalog = {}



# Допишите функцию выборки поддерживаемого девайса из словаря
def get_supported_catalog(dict_devices, device):
    supported_catalog = {}
    if device in dict_devices:
        if device not in not_supported_devices:
            supported_catalog[device] = dict_devices[device]
    return supported_catalog


all_devices = set(mobile_devices.keys()).union(set(home_devices.keys()))
supported_devices = all_devices.difference(not_supported_devices)

for device in all_devices:
    supported_mob_dev = get_supported_catalog(mobile_devices, device)
    # Добавьте значение в словарь result_catalog
    result_catalog.update(supported_mob_dev)
    supported_home_dev = get_supported_catalog(home_devices, device)
    # Добавьте значение в словарь result_catalog
    result_catalog.update(supported_home_dev)


print('Каталог поддерживаемых девайсов: ')
print(result_catalog)