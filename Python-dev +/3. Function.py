def check_mail():
    if new_mail > 0:
        print("Пришло письмо, не пропусти!")
    else:
        print("Никто не пишет.")

new_mail = 0
check_mail()
new_mail = 1
check_mail()


def hello(name):
    print(name + ", приветствую тебя!")

hello("Максим")


def hello(name, bonus):
    print(name + ", приветствую тебя! Бери " + bonus)

hello("Дарт Вейдер", "печеньки")
hello("Винни Пух", "мёд")


def print_home(name='Инкогнито', planet='Икс'):
    print(name + ' живёт на планете ' + planet)

print_home(planet='Земля')  


flat = [
    5.55, 22.19, 7.78, 26.86, 5.55,
    29.84, 22.19, 5.55, 16.85, 4.52
]

room_size = 22.19
count = 0

for room in flat:
    if room == room_size:
        count += 1

print('Комнат площадью', room_size, 'кв.м:', count)


may_2017 = [24, 26, 15, 10, 15, 19, 10, 1, 4, 7, 7, 7, 12, 14, 17, 8, 9, 19, 21, 22, 11, 15, 19, 23, 15, 21, 16, 13, 25, 17, 19]
may_2018 = [20, 27, 23, 18, 24, 16, 20, 24, 18, 15, 19, 25, 24, 26, 19, 24, 25, 21, 17, 11, 20, 21, 22, 23, 18, 20, 23, 18, 22, 23, 11]

def comfort_count(temperatures):
    count = 0
    for temp in temperatures:
        if 22 <= temp <= 26:
            count += 1
    print (f'Количество тёплых дней в этом месяце: {count}')

comfort_count(may_2017)
comfort_count(may_2018)


def calc_cube_perimeter(side):
    return side * 12

def calc_cube_area(side):
    one_face = side * side
    cube_area = one_face * 6
    return cube_area

def calc_cube(side,amount):
    one_cube_perimeter = calc_cube_perimeter(side)
    full_length = one_cube_perimeter * amount

    one_cube_area = calc_cube_area(side)
    full_area = one_cube_area * amount

    print('Для', amount, 'кубов понадобится палок (м):', full_length, 'и стекла (кв.м):', full_area)

calc_cube(3,2)