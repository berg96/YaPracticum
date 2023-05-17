rating = 4.9

# Так вы умеете:
if rating > 4.7:
    print('Фильм крут')
else:
    print('Так себе киношечка')

# А так будет короче:
result = 'Фильм крут' if rating > 4.7 else 'Так себе киношечка'
# В отличие от обычной конструкции if...else 
# тернарный оператор не просто выполняет блок кода, 
# а возвращает значение
print(result)

print('Проверка окончена')