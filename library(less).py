import math 

square_root = math.sqrt(16)
print(square_root)

from random import choice

def find_a_present(prizes):
    return choice(prizes) 

print(find_a_present(['кукла', 'жвачка', 'игрушечный питон']))
print(find_a_present(['мяч', 'чебурашка', 'лосяш']))

from random import choice

answers = ['Норм.', 'Лучше всех :)', 'Ну так', 'Отличненько!', 'Ничего, жить буду']

def how_are_you(answers):
    return choice(answers)

print(how_are_you(answers))

import datetime as dt 

start_time = dt.datetime(1961, 4, 12, 9, 7, 0)

print('Уже', start_time, 'Поехали!') 
landing_time = dt.datetime(1961, 4, 12, 10, 55, 0)
print(landing_time - start_time) 

import datetime as dt

utc_time = dt.datetime.utcnow()
period = dt.timedelta(hours=3)
moscow_time = utc_time + period
print(moscow_time)

import datetime as dt

UTC_OFFSET = {
    'Санкт-Петербург': 3,
    'Москва': 3,
    'Самара': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Пермь': 5,
    'Воронеж': 3,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2
}

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь'
}

def what_time_city(city):
    return dt.datetime.utcnow() + dt.timedelta(hours=UTC_OFFSET[city])

def what_time_friend(friend):
    return what_time_city(DATABASE[friend])

print(what_time_city('Екатеринбург'))
print(what_time_friend('Соня'))