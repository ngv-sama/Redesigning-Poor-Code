# This is a deliberately poorly implemented main script for a Library Management System.

import argparse
from pyfiglet import Figlet

from storage import Session, init_db, init_db_export
from models import Users, Books, Checkout, Admins
from menu import admin_mode, user_mode

# Main Driver Function
def main():
    # Handling CLI interface and parameters
    banner = Figlet(font="doom")
    print(banner.renderText("L i b S y s"))
    
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


    # Verifying Valid Admin
    if(args.mode==0):
        password=args.password
        username=args.username
        if(username==None or password==None):
            print("Username or Password Invalid. Please Try Again")
            return 
        admin_mode(username, password)
    
    # User Mode
    if(args.mode==1):
        user_mode()


    

if __name__ == "__main__":
    # Initializing Database and Main functions
    init_db() 
    main()
