import decimal

result = decimal.Decimal('3.0') + decimal.Decimal('4.0')

# Из модуля decimal импортировать тип данных Decimal
from decimal import Decimal

result = Decimal('3.0') + Decimal('4.0')

# Теперь к типу данных Decimal в коде нужно обращаться по имени Dcml
from decimal import Decimal as Dcml

result = Dcml('3.0') + Dcml('4.0')

# Импортируйте модуль и используйте переименование
import datetime as dt
# Запишите в переменную объект типа хранящего
# и дату, и время 
now_date_time = dt.datetime.now()

print(now_date_time)

# Импортируйте модуль и используйте переименование
import datetime as dt
# Запишите в переменные даты рождения детей
lera_birthday = dt.date(2015, 5, 16)
maxim_birthday = dt.date(2011, 12, 16)

print(lera_birthday)
print(maxim_birthday)

today = dt.date.today()

print(today)

import datetime as dt

lera_birthday = dt.date(2015, 5, 16)
maxim_birthday = dt.date(2011, 12, 16)

today = dt.date.today()

# Обратитесь к значению года
# текущей даты через точечную нотацию
today_year = today.year

# Переопределите значение года на текущий
# для дней рождений ребят
lera_birthday = lera_birthday.replace(year=today_year)
maxim_birthday = maxim_birthday.replace(year=today_year)

# Получите разницу между днями рождения и текущей датой
lera_days_left = lera_birthday - today
maxim_days_left = maxim_birthday - today

print(lera_days_left.days)
print(maxim_days_left.days)

import datetime as dt

def get_days_to_birthday(date_birthday):
    today = dt.date.today()
    today_year = today.year
    date_birthday = date_birthday.replace(year=today_year)
    if date_birthday == today:
        return 0
    elif date_birthday < today:
        date_birthday = date_birthday.replace(year=today_year+1)
        return (date_birthday - today).days
    else:
        return (date_birthday - today).days


lera_birthday = dt.date(2015, 5, 16)
maxim_birthday = dt.date(2011, 12, 16)

print(get_days_to_birthday(lera_birthday))
print(get_days_to_birthday(maxim_birthday))
print(get_days_to_birthday(dt.date.today()))

import datetime as dt
# В эту переменную запишите формат для
# преобразования даты
FORMAT = '%d.%m.%Y'

# Добавьте в объявление функции ещё один параметр - имя
def get_days_to_birthday(name, date_birthday):
    # Преобразуйте полученную строку с датой в объект нужного типа
    date_birthday = dt.datetime.strptime(date_birthday,FORMAT).date()
		
    today = dt.date.today()
    date_birthday = date_birthday.replace(year=today.year)

    if date_birthday < today:
        date_birthday = date_birthday.replace(year=today.year + 1)

    days_to_birthday = date_birthday - dt.date.today()
    return f'{name}, до твоего дня рождения осталось дней: {days_to_birthday.days}'


birthdays = [
    ('Лера', '16.05.2015'),
    ('Максим', '16.12.2011'),
    ('Толя','12.06.2016')
]

# Напечатайте результат вызова функции get_days_to_birthday()
# для каждой пары из списка birthdays 
for name,birthday in birthdays:
    print(get_days_to_birthday(name,birthday))