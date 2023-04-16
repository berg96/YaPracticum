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

words_list = ['раз', 'два', 'три', 'четыре', 'пять', 'вышел', 'зайчик', 'погулять']
new_string = '/'.join(words_list)
print(new_string)

quote_1 = 'Работает? Не трогай'
quote_2 = 'Если твой код работает, значит это хороший код'
quote_3 = 'Лень - главное достоинство программиста'

def penult_word(message):
    return message.split()[-3]

print(penult_word(quote_1))
print(penult_word(quote_2))
print(penult_word(quote_3))

def check_query(query):
    elements  = query.split()
    if elements[0] == 'Анфиса,':
        return 'запрос к Анфисе'
    else:
        return 'запрос к кому-то ещё'

queries = [
    'Анфиса, сколько у меня друзей?',
    'Андрей, ну где ты был?',
    'Андрей, ну обними меня скорей!',
    'Анфиса, кто все мои друзья?'
]

for q in queries:
    result = check_query(q)
    print(q, '-', result)

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        
        return 'У тебя ' + str(count) + ' друзей.'
    elif query == 'Кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return 'Твои друзья: ' + friends_string
    elif query == 'Где все мои друзья?':
        cities_string = ', '.join(set(DATABASE.values()))
        return 'Твои друзья в городах: ' + cities_string
    else:
        return '<неизвестный запрос>'

print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
print(process_anfisa('Где все мои друзья?'))

def print_time(hour, minute, second):
    print(f'На часах {hour}:{minute}:{second}')  # Аргумент должен содержать f-строку

print_time('19', '28', '06')

def calc_stat(listened):
    minutes = 0
    for len_song in listened:
        minutes += len_song
    return (f'Вы прослушали {len(listened)} песен общей продолжительностью {int(minutes/60)} минут.')

print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))

