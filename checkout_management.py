# checkout_management.py

from storage import Session
from models import Users, Books, Checkout

class CheckoutManager:
    def checkout_book(self):
        session = Session()
        user_id = int(input("Enter your User Id: "))
        book_id = int(input("Enter the Book Id: "))
        user = session.query(Users).get(user_id)
        book = session.query(Books).get(book_id)

        if user is None or book is None:
            print("User or book not found, please contact Admin")
            session.close()
            return

        if not book.availability:
            print("This book is currently unavailable.")
            return

        new_checkout = Checkout(user_id=user.id, book_id=book.id)
        session.add(new_checkout)

        book.availability = False
        session.commit()

        print(f"Book '{book.title}' checked out successfully.")
        session.close()

    def check_in(self):
        session = Session()
        book_id = int(input("Enter the Book Id: "))
        book = session.query(Books).filter_by(id=book_id).one_or_none()
        if book is None:
            print("No such book exists.")
            return
        if book.availability:
            print("This book is already checked in.")
            return
        book.availability = True
        session.commit()
        print(f"Book '{book.title}' checked in successfully.")
        session.close()
