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