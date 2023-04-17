import math 

square_root = math.sqrt(16)
print(square_root)

from random import choice

def find_a_present(prizes):
    return choice(prizes) 

print(find_a_present(['кукла', 'жвачка', 'игрушечный питон']))
print(find_a_present(['мяч', 'чебурашка', 'лосяш']))

