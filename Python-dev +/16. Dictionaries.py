# При литеральном объявлении любые коллекции (и словари, в том числе) 
# удобно записывать с переносом строк.
movies = {
    'Матрица': 4.7,
    'Хакеры': 4.3,
    'Трон': 3.8,
    'Кибер': 2.5,
    'Пятая власть': 4.1
}

status_dict = {
    'on': 1,
    0: 'off',
    (0, 1): 'выключатель сломан'
}

empty_dict = {}
print(empty_dict)
# Вывод в терминал: {}
print(type(empty_dict))
# Вывод в терминал: <class 'dict'>

movies = [('Матрица', 4.7), ('Трон', 3.8)]

movies_dict = dict(movies)
print(movies_dict)
# Вывод в терминал: {'Матрица': 4.7, 'Трон': 3.8}

movies = dict.fromkeys(['Матрица', 'Хакеры', 'Трон', 'Кибер'])
print(movies)
# Вывод в терминал: {'Матрица': None, 'Хакеры': None, 'Трон': None, 'Кибер': None}

movies = dict.fromkeys(['Матрица', 'Хакеры', 'Трон', 'Кибер'], 4.8)
print(movies)
# Вывод в терминал: {'Матрица': 4.8, 'Хакеры': 4.8, 'Трон': 4.8, 'Кибер': 4.8}

movie_ratings = [4.7, 5.0, 4.3, 4.0]
movies = ['Матрица', 'Хакеры', 'Трон', 'Кибер']

movies_info = zip(movies, movie_ratings)

print(movies_info)
# Вывод в терминал: <zip object at 0x017D4B48>
# Всё так упаковано, что элементы не видны. Но они есть!
for each in movies_info:
    print(each)

movie_ratings = [4.7, 5.0, 4.3, 4.0]
movies = ['Матрица', 'Хакеры', 'Трон', 'Кибер']

movies_info = zip(movies, movie_ratings)

print(dict(movies_info))
# Вывод в терминал: {'Матрица': 4.7, 'Хакеры': 5.0, 'Трон': 4.3, 'Кибер': 4.0}

# В цикле for перебираем последовательность range(3),
# по очереди передаём значение каждого элемента в переменную num,
# для каждого элемента словаря создаём ключ и значение
new_dict = {'Ключ ' + str(num) : 'Значение ' + str(num) for num in range(3)}

print(new_dict)

# Вывод в терминал: 
# {'Ключ 0': 'Значение 0', 'Ключ 1': 'Значение 1', 'Ключ 2': 'Значение 2'}

movies = ['Матрица', 'Хакеры', 'Трон']
сategory = 'Фантастика в IT'

movies_info = {movie:сategory for movie in movies}

print(movies_info)
# Вывод в терминал:
#{'Матрица': 'Фантастика в IT', 'Хакеры': 'Фантастика в IT', 'Трон': 'Фантастика в IT'}

movies = {
    'Матрица': 4.7,
    'Хакеры': 4.3,
    'Трон': 3.8,
    'Кибер': 2.5,
    'Пятая власть': 4.1
}

# Получение значение элемента словаря с ключем 'Кибер'
print(movies['Кибер'])
# Вывод в терминал: 2.5

movies = {
    'Матрица': {'rating': '4.7', 'review': 'Фильм крут'},
    'Хакеры':  {'rating': '4.5', 'review': 'Смотреть можно'},
    'Трон':  {'rating': '3.8', 'review': 'Смотреть можно'},
    'Кибер':  {'rating': '2.5', 'review': 'Так себе киношечка'},
    'Пятая власть':  {'rating': '4.1', 'review': 'Смотреть можно'},
}

hackers = movies['Хакеры']

print(hackers['rating'], hackers['review'])

movies = {
    'Матрица': {'rating': '4.7', 'review': 'Фильм крут'},
    'Хакеры':  {'rating': '4.5', 'review': 'Смотреть можно'},
    'Трон':  {'rating': '3.8', 'review': 'Смотреть можно'},
    'Кибер':  {'rating': '2.5', 'review': 'Так себе киношечка'},
    'Пятая власть':  {'rating': '4.1', 'review': 'Смотреть можно'},
}

movie = 'Трон'
# Проверка: есть ли фильм с нужным названием в словаре movies:
if movie in movies:
        # Если такой ключ есть - программа выведет сообщение
    print("Информация об этом фильме доступна")        
else:
        # Если ключа с названием фильма нет в словаре, программа
        # выведет соответсвующее сообщение
    print('Информация о фильме отсутствует!')

movies = {
    'Матрица': {'rating': 4.7, 'review': 'Фильм крут'},
    'Хакеры':  {'rating': 4.5, 'review': 'Смотреть можно'},
    'Трон':  {'rating': 3.8, 'review': 'Смотреть можно'},
    'Кибер':  {'rating': 2.5, 'review': 'Так себе киношечка'},
    'Пятая власть':  {'rating': 4.1, 'review': 'Смотреть можно'},
}
# Вызов метода get() с одним обязательным параметром
print(movies.get('Хоббит'))
# Вывод в терминал: None

# Вызов метода get() с двумя аргументами
# Второй аргумент - значение, которое вернётся, если ключ в словаре не найден.
print(movies.get('Хатико', 'Такого фильма нет в словаре'))
# Вывод в терминал: Такого фильма нет в словаре

print(movies.get('Трон'))
# Вывод в терминал: {'rating': 3.8, 'review': 'Смотреть можно'}

movies = {
    'Матрица': 4.7,
    'Хакеры': 4.3,
    'Трон': 3.8,
}

movies['Сеть'] = 4.3
print(movies)
# Вывод в терминал: {'Матрица': 4.7, 'Хакеры': 4.3, 'Трон': 3.8, 'Сеть': 4.3}

movies = {
    'Матрица': 4.7,
    'Хакеры': 4.3,
    'Трон': 3.8,
}

new_movies = {
    'Сеть': 4.1,
    '23': 4.3,
    'Матрица': 5.0,
}

movies.update(new_movies)
print(movies)
# Вывод в терминал: {'Матрица': 4.7, 'Хакеры': 4.3, 'Трон': 3.8, 'Сеть': 4.1, '23': 4.3}

movies = {
    'Матрица': 4.7,
    'Хакеры': 5.0,
    'Трон': 3.8,
    'Кибер': 2.5,
    'Пятая власть':  4.1,
}

del movies['Трон']
del movies['Кибер']
del movies['Пятая власть']

print(movies)
# Вывод в терминал: {'Матрица': 4.7, 'Хакеры': 5.0}

movies = {
    'Матрица': 4.7,
    'Хакеры': 4.3,
    'Трон': 3.8,
    'Кибер': 2.5,
    'Пятая власть': 4.1
}

# При попытке получить значение элемента словаря с ключем 'Сеть'
# вернётся значение по умолчанию - 'Фильм не найден'
movie_pop = movies.pop('Сеть', 'Фильм не найден')
print(movie_pop)
# Вывод в терминал: Фильм не найден

movie_pop = movies.pop('Трон')
print(movie_pop)
# Вывод в терминал: 3.8

print(movies)
# Вывод в терминал: {'Матрица': 4.7, 'Хакеры': 4.3, 'Кибер': 2.5, 'Пятая власть': 4.1}

movies = {
    'Матрица': 4.7,
    'Хакеры': 4.3,
    'Трон': 3.8,
    'Кибер': 2.5,
    'Пятая власть': 4.1
}

keys = movies.keys()
print(keys)
# Вывод в терминал: dict_keys(['Матрица', 'Хакеры', 'Трон', 'Кибер', 'Пятая власть'])

values = movies.values()
print(values)
# Вывод в терминал: dict_values([4.7, 4.3, 3.8, 2.5, 4.1])

movies = {
    'Матрица': 4.7,
    'Хакеры': 4.3,
    'Трон': 3.8,
    'Кибер': 2.5,
    'Пятая власть': 4.1
}

for movie_name in movies:
    print(movie_name)

# Матрица
# Хакеры
# Трон
# Кибер
# Пятая власть