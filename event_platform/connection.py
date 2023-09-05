import psycopg2


# Connect to your postgres DB
try:
    connection = psycopg2.connect(
        database="dbevents",
        user="admin",
        password="123456",
        host="localhost",
        port="5432"
    )
    print("Connected to the database")
except (Exception, psycopg2.Error) as error:
    print(f"Error: {error}")

# Open a cursor to perform database operations
cur = connection.cursor()

# Execute a query
cur.execute("SELECT * FROM event")

# Retrieve query results
records = cur.fetchall()
print(records)
connection.close()