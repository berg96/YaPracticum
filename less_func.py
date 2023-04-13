def say_about():
    print('Привет, я Анфиса!')
    print('Я персональный помощник.')
    print('Я ещё маленькая,')
    print('но постоянно расту и умнею:')
    print('ведь мой код каждый день дописывают!')

say_about()

def print_friends_count(friends_count):
    if friends_count == 0:
        print('У тебя нет друзей')
    elif friends_count == 1:
        print('У тебя', friends_count, 'друг')
    elif friends_count >= 2 and friends_count <= 4:
        print('У тебя', friends_count, 'друга')
    elif friends_count >= 5 and friends_count < 20:
        print('У тебя', friends_count, 'друзей')
    else:
        print('Ого, сколько у тебя друзей! Целых', friends_count)

print_friends_count (0)
print_friends_count(8)

def print_home(name, planet):
    print(name + ' живет на планете ' + planet)

tatooin = 'Татуин'
greeting = 'Да пребудет с тобой Сила!'
my_son = 'Люк, я твой отец!'
luke = 'Люк Скайуокер'

print_home(luke, tatooin) 

def print_home2(name='Инкогнито', planet='Икс'):
    print(name + ' живёт на планете ' + planet)

print_home2('Дроид-убийца')
print_home2(planet='Земля') 
print_home2(planet='Земля', name='Винни Пух')  