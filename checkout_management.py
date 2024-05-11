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
    checkout = Checkout(user_id=user_id, book_id=book_id)
    session.add(checkout)
    session.commit()
    session.close()
    print("Book Checked Out Successfully")


