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