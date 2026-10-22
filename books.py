
import sqlite3
from database import connect_db


# Function to add a new book
def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()

    if not title or not author:
        print("Title and author cannot be empty.")
        return

    try:
        quantity = int(input("Enter quantity: "))

        if quantity < 0:
            print("Quantity cannot be negative.")
            return

    except ValueError:
        print("Please enter a valid number for quantity.")
        return

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO books (title, author, quantity) VALUES (?, ?, ?)",
        (title, author, quantity)
    )

    connection.commit()
    connection.close()

    print("Book added successfully!")


# Function to display all books
def view_books():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT book_id, title, author, quantity FROM books"
    )

    books = cursor.fetchall()
    connection.close()

    if not books:
        print("No books found in the library.")
        return

    print("\n========== LIBRARY BOOKS ==========")

    for book in books:
        print(f"ID: {book[0]}")
        print(f"Title: {book[1]}")
        print(f"Author: {book[2]}")
        print(f"Quantity: {book[3]}")
        print("-----------------------------------")


# Run this file directly for testing
if __name__ == "__main__":
    while True:
        print("\n===== BOOK MANAGEMENT =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            print("Exiting book management.")
            break
        else:
            print("Invalid choice. Please try again.")
