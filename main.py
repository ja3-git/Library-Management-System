
from database import create_tables
from books import add_book, view_books
from members import add_member, view_members
from transactions import (
    issue_book,
    return_book,
    view_transactions
)


def main():
    # Create database tables if they do not exist
    create_tables()

    while True:
        print("\n================================")
        print("   LIBRARY MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add Book")
        print("2. View Books")
        print("3. Register Member")
        print("4. View Members")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. View Transactions")
        print("8. Exit")
        print("================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            add_member()

        elif choice == "4":
            view_members()

        elif choice == "5":
            issue_book()

        elif choice == "6":
            return_book()

        elif choice == "7":
            view_transactions()

        elif choice == "8":
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
