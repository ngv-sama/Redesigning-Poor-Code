# menu.py

from user_management import UserManager
from book_management import BookManager
from checkout_management import CheckoutManager
from storage import init_db_export

class AdminMode:
    def __init__(self):
        self.user_manager = UserManager()
        self.book_manager = BookManager()
        self.checkout_manager = CheckoutManager()

        self.user_management_menu = {
            "List Users": self.user_manager.list_users,
            "Search Users": self.user_manager.search_user,
            "Add New User": self.user_manager.add_new_user,
            "Promote User": self.user_manager.add_new_admin,
            "Edit User": self.user_manager.edit_user,
            "Delete User": self.user_manager.delete_user
        }

        self.book_management_menu = {
            "List Books": self.book_manager.list_all_books,
            "Search Books": self.book_manager.find_book,
            "Check In Books": self.checkout_manager.check_in,
            "Check Out Books": self.checkout_manager.checkout_book,
            "Add New Book": self.book_manager.add_new_book,
            "Edit Book": self.book_manager.edit_book,
            "Delete Book": self.book_manager.delete_book
        }

    def admin_menu(self):
        print("\nLibSys: Library Management System")
        print("1. Book Management")
        print("2. User Management")
        print("3. Database Export")
        print("4. Exit")
        choice = int(input("Enter choice: "))
        return choice

    def func_management_menu(self, management_menu):
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

    def run(self, username, password):
        if not self.user_manager.check_valid(username, password):
            print("Incorrect Username or Password")
            print("Please try again later...")
            return
        while True:
            mode = self.admin_menu()
            if mode == 1:
                self.func_management_menu(self.book_management_menu)
            elif mode == 2:
                self.func_management_menu(self.user_management_menu)
            elif mode == 3:
                init_db_export()
            elif mode == 4:
                return
            else:
                print("Invalid mode")

class UserMode:
    def __init__(self):
        self.book_manager = BookManager()
        self.checkout_manager = CheckoutManager()

        self.user_menu = {
            "List Books": self.book_manager.list_all_books,
            "Search Books": self.book_manager.find_book,
            "Check In Books": self.checkout_manager.check_in,
            "Check Out Books": self.checkout_manager.checkout_book
        }

    def func_management_menu(self, management_menu):
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

    def run(self):
        self.func_management_menu(self.user_menu)
