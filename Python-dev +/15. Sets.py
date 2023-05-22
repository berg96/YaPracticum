# Литерально set объявляется с помощью фигурных скобок.
toys = {'куклы', 'кубики', 'странная штука', 'самолетики', 'мелки'}

for toy in toys:
    print(toy)

# Литеральное объявление множества
movie_ratings_set = {5.0, 4.1, 4.3, 4.7, 4.7, 3.8}
print(movie_ratings_set)
# Вывод в консоль: {5.0, 4.3, 3.8, 4.1, 4.7}
# Порядок элементов не соответствует литералу. 

print(type(movie_ratings_set))
# Вывод в консоль: <class 'set'>

movie_ratings = [5.0, 4.1, 4.3, 4.7, 4.7, 3.8]
# Объявление множества через функцию set()
movie_ratings_set = set(movie_ratings)
print(movie_ratings_set)
# Вывод в консоль: {5.0, 4.3, 3.8, 4.1, 4.7}
# Элементов получилось меньше, чем в исходном списке: неуникальные значения удалены.
# Порядок элементов не соответствует исходному списку. 

print(type(movie_ratings_set))
# Вывод в консоль: <class 'set'>

empty_set = set()
print(empty_set)
# Вывод в терминал: set()
print(type(empty_set))
# Вывод в терминал: <class 'set'>

empty_set = {}
print(type(empty_set))
# Вывод в терминал: <class 'dict'>

movies = ['Матрица', 'Сеть', 'Хакеры', 'Трон', 'Тихушники', 'Сеть', 'Трон']
uniq_movies = set(movies)
print(uniq_movies)
# Вывод в терминал: {'Сеть', 'Матрица', 'Тихушники', 'Хакеры', 'Трон'}
# Дублирующиеся названия удалены!

not_uniq_str = 'съешь же ещё этих мягких французских булок да выпей чаю'
str_without_space = not_uniq_str.replace(" ","")
uniq_str_set = set(str_without_space)
count_char = len(uniq_str_set)
# место для вашего кода
print(count_char)