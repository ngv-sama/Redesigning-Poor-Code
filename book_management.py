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

def find_book():
    session=Session()
    print("\nLibSys: Library Management System")
    print("Search Book By: ")
    print("1. Book Title")
    print("2. Book Author")
    print("3. Book ISBN")
    print("4. Exit")
    choice = int(input("Enter choice: "))

    if(choice==1):
        title = input("Enter Book Title: ")
        query=session.query(Books).filter_by(title=title).all()
        print_query(query)
    elif(choice==2):
        author_name=input("Enter Book Author: ")
        query=session.query(Books).filter_by(author_name=author_name).all()
        print_query(query)
    elif(choice==3):
        isbn=input("Enter Book ISBN: ")
        query=session.query(Books).filter_by(isbn=isbn).all()
        print_query(query)

def print_query(query):
    for book in query:
            print(f"Book ID: {book.id}, Title: {book.title}, Author: {book.author_name}, Availability: {book.availability}")

