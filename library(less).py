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

