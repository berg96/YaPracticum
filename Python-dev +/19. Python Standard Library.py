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