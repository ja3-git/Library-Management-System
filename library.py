import json
import os

FILE_NAME = "books.json"


# Load books from JSON file
def load_books():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save books to JSON file
def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)


# Add a new book
def add_book(books):
    print("\n--- Add Book ---")

    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()

    if title == "" or author == "":
        print("Title and author cannot be empty.")
        return

    book = {
        "title": title,
        "author": author,
        "status": "Available"
    }

    books.append(book)
    save_books(books)

    print("Book added successfully!")


# Display all books
def display_books(books):
    print("\n--- All Books ---")

    if len(books) == 0:
        print("No books in the library.")
        return

    for number, book in enumerate(books, start=1):
        print(
            f"{number}. "
            f"{book['title']} | "
            f"{book['author']} | "
            f"{book['status']}"
        )


# Search for a book
def search_book(books):
    print("\n--- Search Book ---")

    search = input("Enter book title: ").strip().lower()

    found = False

    for book in books:
        if search in book["title"].lower():
            print("\nBook Found")
            print("Title :", book["title"])
            print("Author:", book["author"])
            print("Status:", book["status"])

            found = True

    if not found:
        print("Book not found.")


# Issue a book
def issue_book(books):
    print("\n--- Issue Book ---")

    title = input("Enter book title: ").strip().lower()

    for book in books:

        if book["title"].lower() == title:

            if book["status"] == "Available":
                book["status"] = "Issued"

                save_books(books)

                print("Book issued successfully!")
            else:
                print("Book is already issued.")

            return

    print("Book not found.")


# Return a book
def return_book(books):
    print("\n--- Return Book ---")

    title = input("Enter book title: ").strip().lower()

    for book in books:

        if book["title"].lower() == title:

            if book["status"] == "Issued":
                book["status"] = "Available"

                save_books(books)

                print("Book returned successfully!")
            else:
                print("This book is already available.")

            return

    print("Book not found.")


# Remove a book
def remove_book(books):
    print("\n--- Remove Book ---")

    title = input("Enter book title: ").strip().lower()

    for book in books:

        if book["title"].lower() == title:

            if book["status"] == "Issued":
                print("Cannot remove an issued book.")
                return

            books.remove(book)
            save_books(books)

            print("Book removed successfully!")
            return

    print("Book not found.")


# Main program
def main():

    books = load_books()

    while True:

        print("\n================================")
        print("     LIBRARY MANAGEMENT SYSTEM")
        print("================================")

        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Remove Book")
        print("7. Exit")

        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(books)

        elif choice == "2":
            display_books(books)

        elif choice == "3":
            search_book(books)

        elif choice == "4":
            issue_book(books)

        elif choice == "5":
            return_book(books)

        elif choice == "6":
            remove_book(books)

        elif choice == "7":
            print("\nThank you for using the Library Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start program
if __name__ == "__main__":
    main()