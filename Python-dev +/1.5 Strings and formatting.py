string = 'По Борнео и Ямайке ходит слон в трусах и майке'
new_list = list(string)
new_set = set(string)
print('Список из строки: ' + str(new_list))
print('Сет из строки: ' + str(new_set))


monument_string = 'Я памятник себе воздвиг нерукотворный'

index_list = [0, 1, 2, 8, 6, 17, 24]

for i in index_list:
    # На каждой итерации цикла 
    # берём из строки monument_string элемент с индексом i и печатаем полученную букву
    print(monument_string[i])


friends = ['Сергей', 'Соня', 'Миша', 'Дима', 'Алина']
print(friends[-3])  # Миша
print(friends[-5])  # Сергей

# То же и со строкой
monument_string = 'Я памятник себе воздвиг нерукотворный'
print(monument_string[-2])   # ы
print(monument_string[-37])  # Я 


milk_str = 'молоковоз'

# Применяем метод split() с аргументом 'о':
new_list = milk_str.split('о')

print(new_list)


message = 'У меня опять всё сломалось и не работает соединение с интернетом!!11'

# Разбиваем сообщение по пробелам на слова
words = message.split()
# Проверяем, есть ли ключевые слова в письме
if 'стоимость' in words:
    print('Переслать письмо в отдел биллинга')
elif 'сломалось' in words:
    print('Переслать письмо в техподдержку')
else:
    print('Содержание письма не определено, придётся прочесть самостоятельно')


words_list = ['раз', 'два', 'три', 'четыре', 'пять', 'вышел', 'зайчик', 'погулять']
# Метод join() "склеивает" элементы списка,
# создавая строку, в которой 
# элементы исходного списка разделены текстовым символом;
# для разделения применим дефис:
new_string = '-'.join(words_list)

print(new_string)


weather = 'облачно'
print(f'На улице сейчас {weather}.')