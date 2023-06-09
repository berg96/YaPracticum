name_movie = list('Матрица')
print(name_movie)
# Вывод в терминал: ['М', 'а', 'т', 'р', 'и', 'ц', 'а']

# Такая запись создаст пустой список:
movies = list()
print(movies)
# Вывод в терминал: []

# Литеральное объявление переменных типа int и float:
count = 5
proportion = 4.1

# А вот уже не литеральное объявление переменной:
summa = count + proportion

# При литеральном объявлении строки последовательность символов замыкают в кавычки:
name = 'Игорь'
title = "McDucken’s"

# А нелитеральным объявлением будет, например, объявление строки через функцию:
proportion_str = str(proportion)

# Литералом для объявления списка будет 
# запись элементов через запятую в квадратных скобках
movies = ['Матрица', 'Хакеры', 'Трон']

# Литеральное объявление пустого списка
movie_ratings= []

movie_ratings= [4.7, 5.0, 4.3, 3.8]
# Объявляем новый список, в него будем складывать измененные оценки
new_movie_ratings = []

# Перебор списка в цикле:
for rating in movie_ratings:
    rating += 0.2 # Значение элемента исходного списка увеличивается на 0.2
    new_movie_ratings.append(rating) # Значение добавляется в новый список

print(movie_ratings)
print(new_movie_ratings)
# Вывод в терминал: [4.9, 5.2, 4.5, 4.0]
# Хм, неловко вышло: накрутили рейтинг так, что получили 5.2 по пятибалльной шкале.
# TODO Ладно, позже починим.

movie_ratings = [4.7, 5.0, 4.3, 3.8]
new_movie_ratings = [rating + 0.2 for rating in movie_ratings]
print(new_movie_ratings)

numbers = [i**2 for i in range(1,11)] # Место для вашего кода Создайте список целых чисел 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
print(numbers)


movie_ratings = [4.7, 5.0, 4.3, 3.8]
new_movie_ratings = [
   rating + 0.2 if rating < 4.9 else rating for rating in movie_ratings
]
print(new_movie_ratings)
# Вывод в терминал: [4.9, 5.0, 4.5, 4.0]

movie_ratings = [4.7, 5.0, 4.3, 3.8]
new_movie_ratings = [rating for rating in movie_ratings if rating > 4.5]
print(new_movie_ratings)
# Вывод в терминал:[4.7, 5.0]


week = [
    'Понедельник', 'Вторник', 'Среда', 
    'Четверг', 'Пятница', 'Суббота', 'Воскресенье'
]

mon, tue, wed, thu, fri, sat, sun = week

print(wed)
# Вывод в терминал: Среда

movies = ['Матрица', 'Хакеры', 'Трон']

# Бессмысленно присваивать результат работы метода переменной
new_movies = movies.append('Тихушники')

print(new_movies)
# Вывод в терминал: None

# Метод и не должен был ничего возвращать, он молодец, он выполнил свою работу: 
# изменил исходный список. 
print(movies)
# Вывод в терминал: ['Матрица', 'Хакеры', 'Трон', 'Тихушники']


movie_ratings = [4.7, 5.0, 4.3, 3.8]
movies = ['Матрица', 'Хакеры', 'Трон']
print(id(movies))
# Вывод в терминал: 2217539360448

movies.extend(movie_ratings)
print(movies)
# Вывод в терминал: ['Матрица', 'Хакеры', 'Трон', 4.7, 5.0, 4.3, 3.8]
print(id(movies))
# Вывод в терминал: 2217539360448

# А при конкатенации в памяти будет создан новый объект, а не изменён существующий:
movies = movies + movie_ratings

print(movies)
# Вывод в терминал: ['Матрица', 'Хакеры', 'Трон', 4.7, 5.0, 4.3, 3.8]
print(id(movies))
# Вывод в терминал: 2217540656384
# Другой ID - другой объект.

movies = ['Матрица', 'Хакеры', 'Трон']
movies.insert(1, 'Тихушники')
print(movies)
# Вывод в терминал: ['Матрица', 'Тихушники', 'Хакеры', 'Трон']

movies = ['Матрица', 'Тихушники', 'Хакеры', 'Трон']
movies.remove('Хакеры')
print(movies)
# Вывод в терминал: ['Матрица', 'Тихушники', 'Трон']

# Попытка удалить несуществующий объект
# вызовет исключение
#movies.remove('Сеть')
# Вывод в терминал: ValueError: list.remove(x): x not in list

movies = ['Матрица', 'Тихушники', 'Хакеры', 'Трон']
movie = movies.pop(2)
print(movie)
# Вывод в терминал: Хакеры
print(movies)
# Вывод в терминал: ['Матрица', 'Тихушники', 'Трон']

movie_ratings = [4.7, 5.0, 4.3, 3.8]
rating = movie_ratings.index(4.3)
print(rating)
# Вывод в терминал: 2

movie_ratings = [4.7, 5.0, 4.3, 3.8, 4.7, 4.1]
rating_count = movie_ratings.count(4.7)
print(rating_count)
# Вывод в терминал: 2

movie_ratings = [4.7, 5.0, 4.3, 3.8, 4.7, 4.1]
movie_ratings.sort()
print(movie_ratings)
# Вывод в терминал: [3.8, 4.1, 4.3, 4.7, 4.7, 5.0]

movies = ['Матрица', 'Хакеры', 'Трон']
movies.sort(reverse = True)
print(movies)
# Вывод в терминал: ['Хакеры', 'Трон', 'Матрица']

movie_ratings = [4.7, 5.0, 4.3, 3.8, 4.7, 4.1]
print(id(movie_ratings))
# Вывод в терминал: 27337512

# Разворот списка методом reverse()
movie_ratings.reverse()
print(id(movie_ratings))
# Вывод в терминал: 27337512

print(movie_ratings)
# Вывод в терминал: [4.1, 4.7, 3.8, 4.3, 5.0, 4.7]

movie_ratings = [4.7, 5.0, 4.3, 3.8, 4.7, 4.1]
copy_movie_ratings = movie_ratings.copy()
print(id(movie_ratings))
# Вывод в терминал: 38282024

print(id(copy_movie_ratings))
# Вывод в терминал: 38281640

# Применим сортировку к исходному списку
movie_ratings.sort()
print(movie_ratings)
# Вывод в терминал: [3.8, 4.1, 4.3, 4.7, 4.7, 5.0]

# Элементы списка-копии остались неотсортированными
print(copy_movie_ratings)
# Вывод в терминал: [4.7, 5.0, 4.3, 3.8, 4.7, 4.1]

movie_ratings = [4.7, 5.0, 4.3, 3.8, 4.7, 4.1]
movie_ratings.clear()
print(movie_ratings)
# Вывод в терминал: []

force_words = ['сила', 'пребудет', 'с', 'тобой', 'Да']
print(id(force_words))
# Место для вашего кода
copy = force_words.pop(0)
force_words.insert(0, force_words.pop(-1))
force_words.append(copy)
print(force_words)
# Убедимся, что это тот же объект, что и в начале программы
print(id(force_words))


# Функция tuple() преобразует строку с текстом о достижении в кортеж
achievement = 'Отлично!'
tpl_achiv = tuple(achievement)
print(tpl_achiv)
#Вывод в терминал: ('О', 'т', 'л', 'и', 'ч', 'н', 'о', '!')

# Если передать в функцию неитерируемый объект (например, число),
# Python сообщит, что не может выполнить такое преобразование.
steps = 15000
#tpl_steps = tuple(15000)

#Вывод в терминал: TypeError: 'int' object is not iterable

# Литеральное объявление кортежа
package_1 = ('2:00:01', 15000)

# Значения, перечисленные через запятую и присвоенные одной переменной,
# будут упакованы в кортеж
package_2 = '2:00:01', 15000

print(package_1)
# Вывод в терминал: ('2:00:01', 15000)
print(type(package_1))
# Вывод в терминал: <class 'tuple'>

print(package_2)
# Вывод в терминал: ('2:00:01', 15000)
print(type(package_2))
# Вывод в терминал: <class 'tuple'>

package = ('2:00:01', 15000)

time, steps = package

print(steps)
# Вывод в терминал: 15000
print(time)
# Вывод в терминал: '2:00:01'

not_srtd_tpl = (5**5, 5**2, 5**1, 5**4, 5**0, 5**3)
print(not_srtd_tpl)
# Вывод в терминал: (3125, 25, 5, 625, 1, 125)

srtd_tpl = sorted(not_srtd_tpl)
print(srtd_tpl)
# Вывод в терминал: [1, 5, 25, 125, 625, 3125]
# Отсортировали, но вместо кортежа получили список.
# Исходный кортеж остался неизменённым.

not_srtd_tpl = (5**5, 5**2, 5**1, 5**4, 5**0, 5**3)

# Измените это выражение, чтобы результатом был кортеж
srtd_tpl = tuple(sorted(not_srtd_tpl))
print(srtd_tpl)

days = ('пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс')
steps = [1500, 3445, 13222, 10000, 12555, 1300, 6000]

#result = []
#for i in range(7):
 #   result.append((days[i], steps[i]))

result = [(days[i], steps[i]) for i in range(7)]

# Место для вашего кода

print(result)