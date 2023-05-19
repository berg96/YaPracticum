brand_name = 'Unicorn'
print(id(brand_name))
# Вывод в терминал: 25080896

copy_brand_name = brand_name
print(id(copy_brand_name))
# Вывод в терминал: 25080896
# ID совпадают, значит, обе переменные ссылаются на одну ячейку памяти.