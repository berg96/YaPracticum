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