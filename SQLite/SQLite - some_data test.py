import sqlite3

name = input("what is your name?: ")
department = input("what is your department?: ")
salary = int(input("what is your salary?: "))

db_connection = sqlite3.connect("some_data.db")

cursor = db_connection.cursor()

createTable = '''create table if not exists users(
id integer primary key autoincrement,
name text not null,
department text not null,
salary integer
) STRICT'''

cursor.execute(createTable)
db_connection.commit()

addData = '''insert into users (name,department,salary) values (?,?,?)'''
cursor.execute(addData,(name,department,salary))
db_connection.commit()

fetchData = '''select * from users'''
cursor.execute(fetchData)
rowsInTable = cursor.fetchall()
for row in rowsInTable:
    print(row)


cursor.close()
db_connection.close()