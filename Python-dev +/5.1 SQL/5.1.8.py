import sqlite3

con = sqlite3.connect('db_video.sqlite')
cur = con.cursor()

results = cur.execute(
    '''
    SELECT title,
           release_year
    FROM video_products
    WHERE release_year > 1980
    ORDER BY release_year;
'''
)

for result in results:
    print(result)

results = cur.execute(
    '''
    SELECT product_type,
           title
    FROM video_products
    WHERE release_year > 1980
    ORDER BY product_type DESC, title;
'''
)

for result in results:
    print(result)

con.close()
