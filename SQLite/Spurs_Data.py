import sqlite3

db_connection = sqlite3.connect("Spurs_Database.csv")
cursor = db_connection.cursor()
createTable = '''create table if not exists users(
id integer primary key autoincrement,
name text not null,
year integer,
appearances integer,
goal integer
) STRICT'''

cursor.execute(createTable)
db_connection.commit()

addData = '''insert into users (name,year,appearances,goal) values (?,?,?,?)'''
db_connection.commit()

y = open('Spurs_Data.csv','r')
y.readline() #read in the header line which has no data for the table
for line in y:
    line = line.strip() # remove the newline character
    db = tuple(line.split(',')) #create a tuple for the database
    #create a docstring which contains the SQL command for the cursor to run
    cursor.execute(addData,db)
    #save the changes to the database
    db_connection.commit()

fetchData = '''select * from users'''
cursor.execute(fetchData)
rowsInTable = cursor.fetchall()
for row in rowsInTable:
    print(row)
        
cursor.close()
db_connection.close()