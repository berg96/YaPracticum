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