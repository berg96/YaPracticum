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