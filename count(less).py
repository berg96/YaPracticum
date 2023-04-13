flat = [
    5.55, 22.19, 7.78, 26.86, 5.55,
    29.84, 22.19, 5.55, 16.85, 4.52
]

rooms_num = len(flat)

print(rooms_num)

def rooms_equal(room_size,room_list):
    count = 0

    for room in room_list:
        if room == room_size:
            count += 1

    print('Комнат площадью', room_size, 'кв.м:', count)

rooms_equal(5.55, flat)

sum_area = 0

for room in flat:
    sum_area += room

print('Общая площадь =', sum_area)