day_1 = 1.434
day_2 = 2.12
day_3 = 1.632
day_4 = 5.59
day_5 = 2.542
day_6 = 1.1
day_7 = 1.324

week_dist = (day_1*1000 + day_2*1000 +day_3*1000 + day_4*1000 + day_5*1000 + day_6*1000 + day_7*1000) / 1000

print(week_dist)


from decimal import Decimal

i = 3.3 + 4.1
print(i)
# Вывод в терминал: 7.3999999999999995

i = Decimal('3.3') + Decimal('4.1')
print(i)
# Вывод в терминал: 7.4