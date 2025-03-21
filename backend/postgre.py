import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="shubhk2004",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()
cursor.execute("SELECT version();")
print(cursor.fetchone())

cursor.close()
conn.close()
