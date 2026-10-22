
from database import connect_db


# Function to register a new member
def add_member():
    name = input("Enter member name: ").strip()
    contact = input("Enter contact number: ").strip()

    if not name:
        print("Member name cannot be empty.")
        return

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO members (name, contact) VALUES (?, ?)",
        (name, contact)
    )

    connection.commit()
    connection.close()

    print("Member registered successfully!")


# Function to display all members
def view_members():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT member_id, name, contact FROM members"
    )

    members = cursor.fetchall()
    connection.close()

    if not members:
        print("No members registered yet.")
        return

    print("\n========== LIBRARY MEMBERS ==========")

    for member in members:
        print(f"Member ID: {member[0]}")
        print(f"Name: {member[1]}")
        print(f"Contact: {member[2] or 'Not provided'}")
        print("-------------------------------------")


# Menu for testing member management
if __name__ == "__main__":
    while True:
        print("\n===== MEMBER MANAGEMENT =====")
        print("1. Register Member")
        print("2. View Members")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_member()
        elif choice == "2":
            view_members()
        elif choice == "3":
            print("Exiting member management.")
            break
        else:
            print("Invalid choice. Please try again.")
