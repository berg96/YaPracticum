def calc_square(side_a, side_b):
    result = side_a * side_b
    return result

rectangle_area = calc_square(16, 9)

print(rectangle_area)

room1 = calc_square(3, 5)
room2 = calc_square(4, 6)
room3 = calc_square(3, 6)
rooms_sum = room1 + room2 + room3
print('Суммарная площадь комнат равна', rooms_sum, 'кв.м')

def calc_cube_perimeter(side):
    return side * 12

print('Необходимый метраж палок для 8 кубов:', 8*calc_cube_perimeter(3))

def calc_cube_area(side):
    return 6* side * side

print('Необходимая площадь стекла для 8 кубов, кв.м:', 8*calc_cube_area(3))

def calc_cube(side):
    print('Для 8 кубов понадобится палок (м):', 8*calc_cube_perimeter(side), 'и стекла (кв.м):', 8*calc_cube_area(side))

calc_cube(3)