# main.py
# To Access Admin Mode and use all features
# Type the following in the CMDLET:
# python main.py --mode 0 --username 123456 --password 123456


import argparse
from pyfiglet import Figlet
from storage import init_db
from menu import AdminMode, UserMode

class LibrarySystem:
    def __init__(self):
        init_db()
        self.admin_mode = AdminMode()
        self.user_mode = UserMode()

    def main(self):
        banner = Figlet(font="doom")
        print(banner.renderText("L i b S y s"))
        
        parser = argparse.ArgumentParser(prog="Library Management System", description="A tool to help manage the Techolution Digital Library")
        parser.add_argument('--mode', help="Use this CLI in either Admin or User Mode:\n0---> Flag for Admin\n1---> Flag for User", default=1, type=int)
        parser.add_argument('--username', help="Username of Admin to access Admin Mode", type=str)
        parser.add_argument('--password', help="Password of Admin to access Admin Mode", type=str)
        args = parser.parse_args()

        if args.mode == 0:
            if args.username is None or args.password is None:
                print("Username or Password Invalid. Please Try Again")
                return 
            self.admin_mode.run(args.username, args.password)
        elif args.mode == 1:
            self.user_mode.run()

if __name__ == "__main__":
    library_system = LibrarySystem()
    library_system.main()
