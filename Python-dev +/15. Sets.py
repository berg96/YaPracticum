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


# Создаём словарь: коллекцию, каждый элемент которой состоит из пары "ключ:значение"
# Ключами словаря могут быть только хешируемые объекты.
# Каждый ключ в словаре - уникален
movie_info = {'Матрица': 4.5, 'Трон': 4.8}

# В set() передан словарь
movie_names = set(movie_info)
print(movie_names)
# Вывод в терминал: {'Трон', 'Матрица'}
# В результате получилось множество,
# состоящее из ключей исходного словаря

# В set() передан список элементов типа float
movie_ratings = [5.0, 4.1, 4.3, 4.7, 4.7, 3.8]
movie_ratings_set = set(movie_ratings)
# Множество успешно создано
print(movie_ratings_set)
# Вывод в терминал: {5.0, 4.3, 3.8, 4.1, 4.7}

# Один из элементов исходного списка - список (нехешируемый объект)
movie_ratings = [5.0, 4.1, [4.3, 4.7], 4.7, 3.8]
# При преобразовании исходного списка в множество
# программа выдаст ошибку:
#movie_ratings_set = set(movie_ratings)
print(movie_ratings_set)
# Вывод в терминал: TypeError: unhashable type: 'list'

maxim_toys = {'машинка', 'скакалка', 'кубики', 'пистолетик'}
print(id(maxim_toys))
# Вывод в терминал: 33482552

maxim_toys.add('самолётик')
# Проверим что элемент добавлен к исходному множеству
print(id(maxim_toys))
# Вывод в терминал: 33482552
print(maxim_toys)
# Вывод в терминал:{'скакалка', 'машинка', 'самолетик', 'пистолетик', 'кубики'}

# Попробуем добавить ещё кубики в множество:
maxim_toys.add('кубики')
print(maxim_toys)
# Вывод в терминал:{'скакалка', 'машинка', 'самолетик', 'пистолетик', 'кубики'}
# Новый элемент в множестве не появился.

maxim_toys = {'машинка', 'скакалка', 'кубики', 'пистолетик'}

# Удаление существующего элемента
maxim_toys.remove('кубики')
print(maxim_toys)
# Вывод в терминал: {'машинка', 'скакалка', 'пистолетик'}

maxim_toys.discard('машинка')
print(maxim_toys)
# Вывод в терминал: {'скакалка', 'пистолетик'}

# Удаление несуществующих элементов
maxim_toys.discard('кукла')
print(maxim_toys)
# Вывод в терминал: {'скакалка', 'пистолетик'}

#maxim_toys.remove('кукла')
print(maxim_toys)
# Вывод в терминал: KeyError: 'кукла'