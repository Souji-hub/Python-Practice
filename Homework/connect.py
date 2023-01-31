import psycopg2

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="admin",
    
)

conn.autocommit = True  

# Create a cursor
cur = conn.cursor()

# Create the database
cur.execute("DROP DATABASE mydatabase")
cur.execute("CREATE DATABASE mydatabase")

# Close the cursor and connection to the previous database
cur.close()
conn.close()

# Connect to the newly created database
conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="postgres",
    password="admin"
)

# Create a cursor
cur = conn.cursor()

# Create the table
cur.execute("""
    CREATE TABLE mytable (
        id SERIAL PRIMARY KEY NOT NULL,
        name VARCHAR(255) NOT NULL,
        age INTEGER 
    )
""")

# Insert 10 records
records = [
    ("John Doe", 30),
    ("Jane Doe", 25),
    ("Jim Smith", 35),
    ("Emily Davis", 28),
    ("Michael Brown", 40),
    ("Sarah Johnson", 33),
    ("David Lee", 38),
    ("Jessica Wilson", 27),
    ("William Thompson", 32),
    ("Linda Martinez", 29),
]

for name, age in records:
    cur.execute("INSERT INTO mytable (name, age) VALUES (%s, %s)", (name, age))


# reading and inserting sql data from a file

with open("Homework\Database\Person.sql", "r") as f:
    sql = f.read()
    cur.execute(sql)

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
