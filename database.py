
import sqlite3

# Database file name
DATABASE_NAME = "library.db"


# Connect Python to the database
def connect_db():
    connection = sqlite3.connect(DATABASE_NAME)
    return connection


# Create database tables
def create_tables():
    connection = connect_db()
    cursor = connection.cursor()

    # Table for books
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            quantity INTEGER NOT NULL DEFAULT 0
        )
    """)

    # Table for library members
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            member_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact TEXT
        )
    """)

    # Table for issuing and returning books
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER NOT NULL,
            member_id INTEGER NOT NULL,
            issue_date TEXT NOT NULL,
            return_date TEXT,
            FOREIGN KEY (book_id) REFERENCES books(book_id),
            FOREIGN KEY (member_id) REFERENCES members(member_id)
        )
    """)

    connection.commit()
    connection.close()

    print("Database connected successfully!")
    print("All tables created successfully!")


# Run this file directly
if __name__ == "__main__":
    create_tables()
