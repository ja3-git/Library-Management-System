
import sqlite3

connection = sqlite3.connect("library.db")
cursor = connection.cursor()

tables = ["books", "members", "transactions"]

for table in tables:
    print(f"\n===== {table.upper()} =====")

    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    if not rows:
        print("No records found.")

connection.close()
