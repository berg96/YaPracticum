import sqlite3

con = sqlite3.connect('db_video_3.sqlite')
cur = con.cursor()

video_products = [
    (1, 'Безумные мелодии Луни Тюнз', 2),
    (2, 'Весёлые мелодии', 2),
    (3, 'Кто подставил кролика Роджера', 3),
    (4, 'Хороший, плохой, злой', 3),
    (5, 'Последний киногерой', 3),
    (6, 'Она написала убийство', 4),
    (7, 'Миссис Харрис едет в Париж', 3),
]
product_types = [
    (1, 'Мультфильм'),
    (2, 'Мультсериал'),
    (3, 'Фильм'),
    (4, 'Сериал'),
]
cur.executemany('INSERT INTO product_types VALUES(?, ?);', product_types)
cur.executemany('INSERT INTO video_products VALUES(?, ?, ?);', video_products)

con.commit()
con.close()
