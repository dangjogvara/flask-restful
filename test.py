import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)


insert_query = "INSERT INTO users VALUES (?, ?, ?)"

users = [
    (1, 'dan', 'asdf'),
    (2, 'rolf', 'asdf'),
    (3, 'anne', 'asdf')
]

cursor.executemany(insert_query, users)

connection.commit()

connection.close()
