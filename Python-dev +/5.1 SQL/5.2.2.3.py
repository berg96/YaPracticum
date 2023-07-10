import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

results = cur.execute(
    '''
    SELECT video_products.title AS translation,
           original_titles.title AS original
    FROM video_products,
         original_titles
    WHERE 
        video_products.original_title_id = original_titles.id
    AND
        original LIKE 'M%'
'''
)

for result in results:
    print(result)

con.close()
