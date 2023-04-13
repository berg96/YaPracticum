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