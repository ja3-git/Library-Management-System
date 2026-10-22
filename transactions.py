
import sqlite3
from datetime import date
from database import connect_db


# Function to issue a book
def issue_book():
    try:
        book_id = int(input("Enter book ID: "))
        member_id = int(input("Enter member ID: "))
    except ValueError:
        print("Book ID and member ID must be numbers.")
        return

    connection = connect_db()
    cursor = connection.cursor()

    try:
        # Check whether the book exists and is available
        cursor.execute(
            "SELECT title, quantity FROM books WHERE book_id = ?",
            (book_id,)
        )
        book = cursor.fetchone()

        if book is None:
            print("Book not found.")
            return

        if book[1] <= 0:
            print("This book is currently unavailable.")
            return

        # Check whether the member exists
        cursor.execute(
            "SELECT name FROM members WHERE member_id = ?",
            (member_id,)
        )
        member = cursor.fetchone()

        if member is None:
            print("Member not found.")
            return

        # Save the issue transaction
        issue_date = date.today().isoformat()

        cursor.execute("""
            INSERT INTO transactions
            (book_id, member_id, issue_date, return_date)
            VALUES (?, ?, ?, NULL)
        """, (book_id, member_id, issue_date))

        # Reduce available book quantity
        cursor.execute("""
            UPDATE books
            SET quantity = quantity - 1
            WHERE book_id = ? AND quantity > 0
        """, (book_id,))

        if cursor.rowcount != 1:
            connection.rollback()
            print("Book is no longer available.")
            return

        connection.commit()
        print(f"Book '{book[0]}' issued to {member[0]} successfully!")
        print(f"Issue date: {issue_date}")

    except sqlite3.Error as error:
        connection.rollback()
        print("Database error:", error)

    finally:
        connection.close()


# Function to return a book
def return_book():
    try:
        transaction_id = int(
            input("Enter transaction ID to return: ")
        )
    except ValueError:
        print("Transaction ID must be a number.")
        return

    connection = connect_db()
    cursor = connection.cursor()

    try:
        # Find an unreturned transaction
        cursor.execute("""
            SELECT book_id, member_id
            FROM transactions
            WHERE transaction_id = ? AND return_date IS NULL
        """, (transaction_id,))

        transaction = cursor.fetchone()

        if transaction is None:
            print("Active transaction not found.")
            return

        book_id = transaction[0]

        # Mark the transaction as returned
        return_date = date.today().isoformat()

        cursor.execute("""
            UPDATE transactions
            SET return_date = ?
            WHERE transaction_id = ? AND return_date IS NULL
        """, (return_date, transaction_id))

        if cursor.rowcount != 1:
            connection.rollback()
            print("This transaction has already been returned.")
            return

        # Increase available book quantity
        cursor.execute("""
            UPDATE books
            SET quantity = quantity + 1
            WHERE book_id = ?
        """, (book_id,))

        connection.commit()
        print("Book returned successfully!")
        print(f"Return date: {return_date}")

    except sqlite3.Error as error:
        connection.rollback()
        print("Database error:", error)

    finally:
        connection.close()


# Function to view all transactions
def view_transactions():
    connection = connect_db()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT
                t.transaction_id,
                b.title,
                m.name,
                t.issue_date,
                t.return_date
            FROM transactions AS t
            JOIN books AS b ON t.book_id = b.book_id
            JOIN members AS m ON t.member_id = m.member_id
            ORDER BY t.transaction_id
        """)

        transactions = cursor.fetchall()

        if not transactions:
            print("No transactions found.")
            return

        print("\n========== TRANSACTION HISTORY ==========")

        for item in transactions:
            status = item[4] if item[4] else "Not returned"

            print(f"Transaction ID: {item[0]}")
            print(f"Book: {item[1]}")
            print(f"Member: {item[2]}")
            print(f"Issue date: {item[3]}")
            print(f"Return date/status: {status}")
            print("-----------------------------------------")

    except sqlite3.Error as error:
        print("Database error:", error)

    finally:
        connection.close()


# Menu for testing transactions
if __name__ == "__main__":
    while True:
        print("\n===== BOOK TRANSACTIONS =====")
        print("1. Issue Book")
        print("2. Return Book")
        print("3. View Transactions")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            issue_book()
        elif choice == "2":
            return_book()
        elif choice == "3":
            view_transactions()
        elif choice == "4":
            print("Exiting transaction management.")
            break
        else:
            print("Invalid choice. Please try again.")
