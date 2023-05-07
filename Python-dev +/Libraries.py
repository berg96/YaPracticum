import math 

# Теперь в программе можно применять любые функции из неё.
square_root = math.sqrt(16)
print(square_root)


from random import choice  # Импорт одной функции из библиотеки

def find_a_present(prizes):
    # Обращаемся к функции напрямую: choice(), а не random.choice()
    return choice(prizes) 

print(find_a_present(['кукла', 'жвачка', 'игрушечный питон']))
print(find_a_present(['мяч', 'чебурашка', 'лосяш']))


import random as r

# Теперь к библиотеке random нужно обращаться только через псевдоним r:
print(r.randint(0, 100)) # Случайное целое число от 0 до 100


import datetime as dt 

# Взлёт: 1961 год, 12 апреля, 9 часов утра, 7 минут 
start_time = dt.datetime(1961, 4, 12, 9, 7, 0)

print('Уже', start_time, 'Поехали!') 

landing_time = dt.datetime(1961, 4, 12, 10, 55, 0)

print(landing_time - start_time) 


import datetime as dt

start_moment = dt.datetime(2023, 4, 29, 18, 19)  # Напишите код здесь
current_moment = dt.datetime(2023, 5, 7, 19, 39)  # и здесь

total_time = current_moment - start_moment  # и здесь

print(total_time)