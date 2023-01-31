import psycopg2

# Connect to the server
cons = psycopg2.connect(
    host='localhost',
    user="postgres",
    password="admin"
)

# Create a database
cus = cons.cursor()
cus.execute('CREATE DATABASE database1')

#database connection
cond = psycopg2.connect(
    host = 'localhost',
    user='postgres',
    password = 'admin',
    database = 'database1'
)
# add data to database
cud = cond.cursor()
cud.execute('CREATE TABLE mytable1(id SERIAL PRIMARY KEY, name VARCHAR(255), age INTEGER)')
cud.execute()

cond.close()
cus.close()
cons.close()