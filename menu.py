import book_management
import user_management
import checkout_management
from storage import Session, init_db, init_db_export

user_management_menu = {
    "List Users": user_management.list_users,
    "Search Users": user_management.search_user,
    "Add New User": user_management.add_new_user,
    "Promote User": user_management.add_new_admin,
    "Edit User": user_management.edit_user,
    "Delete User": user_management.delete_user
}

book_management_menu = {
    "List Books": book_management.list_all_books,
    "Search Books": book_management.find_book,
    "Check In Books": checkout_management.check_in,
    "Check Out Books": checkout_management.checkout_book,
    "Add New Book": book_management.add_new_book,
    "Edit Book": book_management.edit_book,
    "Delete Book": book_management.edit_book
}

user_menu = {
    "List Books": book_management.list_all_books,
    "Search Books": book_management.find_book,
    "Check In Books": checkout_management.check_in,
    "Check Out Books": checkout_management.checkout_book
}

def admin_menu():
    print("\nLibSys: Library Management System")
    print("1. Book Management")
    print("2. User Management")
    print("3. Database Export")
    print("4. Exit")
    choice = int(input("Enter choice: "))
    return choice

def func_management_menu(management_menu):
    while True:
        print("\nLibSys Dashboard")
        management_keys = list(management_menu.keys())  # Convert dict_keys to list
        for i in range(len(management_keys)):
            print(f"{i}. {management_keys[i]}")
        print(f"{i+1}. Back")
        choice = int(input("Enter choice: "))
        try:
            if choice == i+1:
                return
            else:
                management_menu[management_keys[choice]]()  # Use choice to index management_keys
        except KeyError:
            print("Invalid Option")
        except IndexError:
            print("Invalid Option")

# Switch Case for Admin Mode
def admin_mode(username, password):
    if not user_management.check_valid(username, password):
        print("Incorrect Username or Password")
        print("Please try again later...")
        return
    while True:
        mode = admin_menu()
        if mode == 1:
            func_management_menu(book_management_menu)
        elif mode == 2:
            func_management_menu(user_management_menu)
        elif mode == 3:
            init_db_export()
        elif mode == 4:
            return
        else:
            print("Invalid mode")

# Switch Case for User Mode
def user_mode():
    while True:
        func_management_menu(user_menu)
        return
