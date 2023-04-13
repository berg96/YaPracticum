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

def number_of_occurrences(char, string):
    count=0
    for letter in string:
        if letter==char:
            count+=1

    print('Исходная строка:', string)
    print('Количество вхождений символа', char, 'составляет:', count)
    

phrase = 'Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили.'

number_of_occurrences('е', phrase)

may_2017 = [24, 26, 15, 10, 15, 19, 10, 1, 4, 7, 7, 7, 12, 14, 17, 8, 9, 19, 21, 22, 11, 15, 19, 23, 15, 21, 16, 13, 25, 17, 19]
may_2018 = [20, 27, 23, 18, 24, 16, 20, 24, 18, 15, 19, 25, 24, 26, 19, 24, 25, 21, 17, 11, 20, 21, 22, 23, 18, 20, 23, 18, 22, 23, 11]

def comfort_count(temperatures):
    count=0
    for temp in temperatures:
        if 22<=temp<=26:
            count+=1
    print('Количество тёплых дней в этом месяце:',count)

comfort_count(may_2017)  # Узнаем, что было в мае 2017 г.
comfort_count(may_2018)  # Узнаем, что было в мае 2018 г.