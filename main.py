# This is a deliberately poorly implemented main script for a Library Management System.

import argparse
from pyfiglet import Figlet

from storage import Session, init_db, init_db_export
from models import Users, Books, Checkout, Admins

import book_management
import user_management
import checkout_management



def admin_menu():
    print("\nLibSys: Library Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Search Books")
    print("4. Add New User")
    print("5. Add New Admin")
    print("6. Checkout Book")
    print("7. Checkin Book")
    print("8. Export Database")
    print("9. Delete Books")
    print("10. List All Users")
    print("11. Delete Users")
    print("12. Exit")
    choice = int(input("Enter choice: "))
    return choice

def user_menu():
    print("\nLibSys: Library Management System")
    print("1. List Books")
    print("2. Checkout Book")
    print("3. Checkin Book")
    print("4. Search Books")
    print("5. Exit")
    choice = int(input("Enter choice: "))
    return choice


def admin_mode(username, password):
    if(not user_management.check_valid(username, password)):
        print("Incorrect Username or Password")
        print("Please try again later...")
        return
    while True:
        mode=admin_menu()
    
        try:
            if mode == 12:
                print("Initiating Exit...")
                return
            elif mode==1:
                book_management.add_new_book()
            elif mode==2:
                book_management.list_all_books()
            elif mode==3:
                book_management.find_book()
            elif mode==4:
                user_management.add_new_user()
            elif mode==5:
                user_management.add_new_admin()
            elif mode==6:
                checkout_management.checkout_book()
            elif mode==7:
                checkout_management.check_in()
            elif mode==8:
                init_db_export()
            elif mode==9:
                book_management.delete_book()
            elif mode==10:
                user_management.delete_user()
            elif mode==11:
                user_management.list_users()

        except KeyError:
            print("Invalid mode")
        
    
        

def user_mode():
    while True:
        mode=user_menu()
        print(mode)

        try:
            if mode == 5:
                print("Initiating Exit...")
                return
                
            elif mode==1:
                book_management.list_all_books()
            elif mode==2:
                checkout_management.checkout_book()
            elif mode==3:
                checkout_management.check_in()
            elif mode==4:
                book_management.find_book()
        except KeyError:
            print("Invalid mode")
        
        



def main():
    banner = Figlet(font="doom")
    print("\n")
    print(banner.renderText("L i b S y s"))
    print("\n")
    
    parser=argparse.ArgumentParser(prog="Library Management System", description="A tool to help manage the Techolution Digital Library")

    parser.add_argument('--mode', help="""
                        Use this CLI in either Admin or User Mode:
                        0---> Flag for Admin
                        1---> Flag for User 
                        """,default=1, type=int)
    
    parser.add_argument('--username', help="""
                        Username of Admin to access Admin Mode
                        """, type=str)
    
    parser.add_argument('--password', help="""
                        Password of Admin to access Admin Mode
                        """, type=str)
    
    args=parser.parse_args()

    if(args.mode==0):
        password=args.password
        username=args.username
        if(username==None or password==None):
            print("Username or Password Invalid. Please Try Again")
            return 
        admin_mode(username, password)
    
    if(args.mode==1):
        user_mode()


    

if __name__ == "__main__":
    init_db()
    main()
