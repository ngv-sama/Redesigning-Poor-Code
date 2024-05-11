# Global list to store books
from storage import Session, init_db
from models import  Users, Books, Checkout, Admins


def add_new_book():
    session=Session()
    title=input("Enter Book Title: ")
    isbn=input("Enter Book ISBN: ")
    language=input("Enter Book Language: ")
    author_id=input("Author: ")
    new_book= Books(title=title, isbn=isbn, language=language, author_name=author_id)
    session.add(new_book)
    session.commit()
    session.close()
    print("Book Added to Database Successfully")

def list_all_books():
    session=Session()
    books = session.query(Books).all()
    for book in books:
        print(f"Book ID: {book.id}, Title: {book.title}, Author: {book.author_name}")
    session.close()

