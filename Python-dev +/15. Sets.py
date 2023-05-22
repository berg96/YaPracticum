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