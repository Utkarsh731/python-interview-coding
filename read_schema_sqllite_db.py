import sqlite3

# Connect to the database
conn = sqlite3.connect("models.db")
cursor = conn.cursor()

# Get a list of all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# For each table, print its schema
for table in tables:
    cursor.execute(f"PRAGMA table_info({table[0]});")
    print(f"Table: {table[0]}")
    print("Column name | Data type | Nullable | Primary key")
    for column in cursor.fetchall():
        print(f"{column[1]} | {column[2]} | {column[3]} | {column[5]}")
    print("\n")

# Close the connection
conn.close()
