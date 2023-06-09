# При указании значения по умолчанию 
# пробелы вокруг оператора в выражении b=1 не нужны. Так говорит PEP8.
def get_mod_diff(a, b=1):
    """Функция возвращает результат разницы полученных значений по модулю."""
    diff = abs(a - b)
    return diff

x = 3
y = 4
print(get_mod_diff(x))
# Вывод в терминал: 2

def get_mod_diff(a, b=1):
    """Функция возвращает результат разницы полученных значений по модулю."""
    diff = abs(a - b)
    return diff

x = 3
y = 4
# Именованные аргументы можно передавать в любом порядке, функция всё поймёт и примет.
print(get_mod_diff(b=y, a=x))

x = [10, 22, 334]
y = [*x, 4, 5, 6]
print(y) 
# Вывод в терминал: [10, 22, 334, 4, 5, 6]

# В функции get_boost() первый аргумент - позиционный,
# а остальные будут распакованы в последовательность с именем ratings
def get_boost(coeff, *ratings):
    for rating in ratings:
        print(coeff + rating)

x = 0.2
# Вызываем функцию и передаём в неё шесть аргументов
# Первый аргумент будет передан в параметр coeff, 
# а остальные будут преобразованы в последовательность
get_boost(x, 4.3, 4.5, 3.0, 2.5, 4.7)
# Вывод в терминал:
# 4.5
# 4.7
# 3.2
# 2.7
# 4.9

def print_profile(character, **info):
    print(f'Персонаж: {character}')
    for key, value in info.items():
        print(f'{key}: {value}')

print_profile('Spider-man',
              name='Питер Паркер',
              talent=['Суперсила', 'Паучье чутье', 'Паутина'],
              сity='Нью-Йорк')
# Вывод в терминал:
# Персонаж: Spider-man
# name: Питер Паркер
# talent: ['Суперсила', 'Паучье чутье', 'Паутина']
# сity: Нью-Йорк

def get_mean(values):
    # Место для вашего кода
    avr_num = 0
    for num in values:
        avr_num += num
    return avr_num/len(values)

# Список значений для теста
num_lst = [3, 6, 5, 7, 9, 1]
# Тут вызов функции.
print(f'{get_mean(num_lst):.2f}')  # Напечатайте результат вызова функции.

def test_range(start, end, *nums): # Укажите параметры
    # место для вашего кода
    result = []
    for num in nums:
        if num >= start and num <= end:
            result.append(num)
        else:
            print ('Число за границами диапазона')
    return result

start = 4
end = 12
print(test_range(start, end, 5, 16, 32, 6, 7, 1))