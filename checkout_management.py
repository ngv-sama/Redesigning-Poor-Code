from storage import Session, init_db
from models import Users, Books, Checkout, Admins

def checkout_book():
    session=Session()
    user_id=input("Enter your User Id: ")
    book_id=input("Enter the Book Id: ")
    user_id = session.query(Users).get(user_id)
    book_id=session.query(Books).get(book_id)
    if(user_id==None or book_id==None):
        print("User not found, please contact Admin")
        session.close()
        return
    
    book = session.query(Books).filter_by(id=book_id).one_or_none()
    if book is None:
        print("No such book exists.")
        return
    if not book.availability:
        print("This book is currently unavailable.")
        return

    
    new_checkout = Checkout(user_id=user_id, book_id=book_id)
    session.add(new_checkout)

    book.availability = False
    session.commit()

    print(f"Book '{book.title}' checked out successfully.")



def check_in():
    session=Session()
    book_id = input("Enter the Book Id: ")
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



