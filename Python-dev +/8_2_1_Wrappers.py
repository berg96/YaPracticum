import time


def sleep_one_sec():
    time.sleep(1)
    return 'Результат первой функции.'


def sleep_two_sec():
    time.sleep(2)
    return 'Результат второй функции.'


def time_of_function(func):
    def wrapper():
        start_time = time.time()
        print('Время пошло')
        result = func()
        execution_time = round(time.time() - start_time, 1)
        print(f'Через {execution_time} сек. функция вернула «{result}»')
        return result

    return wrapper


sleep_one_sec

# Вызов исходной функции.
sleep_one_sec()

# Декорированная исходная функция.
time_of_function(sleep_one_sec)

# Вызов декорированной исходной функции.
time_of_function(sleep_one_sec)()

# Распечатка вызова декорированной функции.
print(time_of_function(sleep_one_sec)())

time_of_function(sleep_one_sec)()
time_of_function(sleep_two_sec)()
