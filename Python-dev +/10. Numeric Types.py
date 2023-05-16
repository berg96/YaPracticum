day_1 = 1.434
day_2 = 2.12
day_3 = 1.632
day_4 = 5.59
day_5 = 2.542
day_6 = 1.1
day_7 = 1.324

week_dist = (day_1*1000 + day_2*1000 +day_3*1000 + day_4*1000 + day_5*1000 + day_6*1000 + day_7*1000) / 1000

print(week_dist)


from decimal import Decimal

i = 3.3 + 4.1
print(i)
# Вывод в терминал: 7.3999999999999995

i = Decimal('3.3') + Decimal('4.1')
print(i)
# Вывод в терминал: 7.4

x = 121 / 7
print(type(x)) 


# Получаем данные в секундах
response = 424562
# Переведите полученное значение в необходимые единицы измерения

seconds = response % 60
minutes = (response // 60) % 60
hours = ((response // 60) // 60) % 24
days = (response // 60 // 60) // 24

print(days, hours, minutes, seconds)


weight = 75  # Вес
height = 175 # Рост
dist = 9.75  # Расстояние в км
hours = 2    # Время движения в часах

spent_calories = (0.035 * weight + (((dist/hours) ** 2) / height) * (0.029 * weight)) * hours * 60# Напишите формулу расчета

print(spent_calories) 