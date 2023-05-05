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