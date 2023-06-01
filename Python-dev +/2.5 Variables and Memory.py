brand_name = 'Unicorn'
print(id(brand_name))
# Вывод в терминал: 25080896

copy_brand_name = brand_name
print(id(copy_brand_name))
# Вывод в терминал: 25080896
# ID совпадают, значит, обе переменные ссылаются на одну ячейку памяти.

brand_name = 'Unicorn'
print(id(brand_name))
# Вывод в терминал: 25080896

brand_name = 'Cat'
print(id(brand_name))
# Вывод в терминал: 27193914
# ID разные: теперь brand_name ссылается на другую ячейку памяти.

brand_info = ['Unicorn', 2]
print(id(brand_info))
# Вывод в терминал: 34153256

# Изменяем значение элемента списка с индексом 1
brand_info[1] = 3
print(brand_info)
# Вывод в терминал: ['Unicorn', 3]
# Значение объекта изменилось. А что с ID?
print(id(brand_info))
# Вывод в терминал: 34153256
# ID остался прежним.

# Объявляем переменную неизменяемого типа str
brand_name = 'Unicorn'
print(id(brand_name))
# Вывод в терминал: 25080896

# Присваиваем новой переменной 
# то же самое значение
new_brand_name = 'Unicorn'
print(id(new_brand_name))
# Вывод в терминал: 25080896
# Снова тот же ID!

# Объявляем переменную изменяемого типа list
steps_weekends_1 = [13300, 12311]
print(id(steps_weekends_1))
# Вывод в терминал: 38675176

# Присваиваем новой переменной 
# то же самое значение
steps_weekends_2 = [13300, 12311]
print(id(steps_weekends_2))
# Вывод в терминал: 38674792
# Значения одинаковые, но ID - разные!

int_hash = hash(5)
print(f'Хеш для числа 5 будет равен {int_hash}')
# Вывод в терминал: Хеш для числа 5 будет равен 5

float_hash = hash(5.123)
print(f'Хеш для числа 5.123 будет равен {float_hash}')
# Вывод в терминал: Хеш для числа 5.123 будет равен 1775969997

string_hash = hash('Строка')
print(f'Хеш для строки "Строка" будет равен {string_hash}')
# Вывод в терминал: Хеш для строки "Строка" будет равен 1577989931