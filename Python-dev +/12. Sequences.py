name_movie = 'Джонни Мнемоник'
# Место для вашего кода

print(name_movie[0])
print(name_movie[2])
print(name_movie[10])
print(name_movie[-2])
print(name_movie[-1])


a = 'Роботы стали важны'
b = 'в период'
c = 'эмиграции с Терры'

print(a[4:7]+b[2]+b[4]+a[1]+c[3:6]+c[1]+c[1:3]+a[7:9])


recommended_movies = ['Хатико', '23', 'Достучаться до небес',
                      'Хакеры', 'Трон', '1408']

hackers_movies = ['Трон', 'Военные игры', 'Тихушники',
                  'Джонни Мнемоник', 'Хакеры', 'Нирвана',
                  '23', 'Враг государства', 'Взлом',
                  'Пароль рыба-меч', 'Сеть', 'Кто я']

# Место для вашего кода.
for movie in recommended_movies:
    if movie in hackers_movies:
        print(f'Разработчикам рекомендуем посмотреть фильм "{movie}"')


simple_range = range(1, 10, 2)
print(simple_range)

# Вывод в терминал: range(1, 10, 2)
# А где числа-то?