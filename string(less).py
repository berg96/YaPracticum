string = 'По Борнео и Ямайке ходит слон в трусах и майке'
new_list = list(string)
new_set = set(string)
print('Список из строки: ' + str(new_list))
print('Сет из строки: ' + str(new_set))

monument_string = 'Я памятник себе воздвиг нерукотворный'

index_list = [0, 1, 2, 8, 6, 17, 24]

for i in index_list:
    print(monument_string[i])

friends = ['Сергей', 'Соня', 'Миша', 'Дима', 'Алина']
print(friends[-3])
print(friends[-5])

monument_string = 'Я памятник себе воздвиг нерукотворный'
print(monument_string[-2])
print(monument_string[-37])

counter_str = 'Раз-два-три-четыре-пять, вышел зайчик погулять'
counter_list = counter_str.split('-')
print(counter_list)

blok_str = 'Ночь. Улица. Фонарь. Аптека'
blok_list = blok_str.split('. ')
print(blok_list)

message = 'У меня опять всё сломалось и не работает соединение с интернетом!!11'
words = message.split()
if 'стоимость' in words:
    print('Переслать письмо в отдел биллинга')
elif 'сломалось' in words:
    print('Переслать письмо в техподдержку')
else:
    print('Содержание письма не определено, придётся прочесть самостоятельно') 

