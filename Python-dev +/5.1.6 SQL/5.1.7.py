import sqlite3

con = sqlite3.connect('db_video.sqlite')
cur = con.cursor()

# Напишите SQL запрос в строке.

cur.execute('''
    SELECT tbl_name
    FROM sqlite_master
    WHERE type='table';
''')

table = cur.fetchall()[0][0]
print(table)

# Напишите SQL запрос в строке.
results = cur.execute(f'''
    SELECT title, release_year
    FROM {table};
''')


for result in results:
    print(result)

con.close()
