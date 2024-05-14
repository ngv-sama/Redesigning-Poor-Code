# book_management.py

from storage import Session
from models import Books

class BookManager:
    def add_new_book(self):
        session = Session()
        title = input("Enter Book Title: ")
        isbn = input("Enter Book ISBN: ")
        language = input("Enter Book Language: ")
        author_id = input("Author: ")
        new_book = Books(title=title, isbn=isbn, language=language, author_name=author_id)
        session.add(new_book)
        session.commit()
        session.close()
        print("Book Added to Database Successfully")

    def list_all_books(self):
        session = Session()
        books = session.query(Books).all()
        for book in books:
            print(f"Book ID: {book.id}, Title: {book.title}, Author: {book.author_name}, Available: {book.availability}")
        session.close()

    def find_book(self):
        session = Session()
        print("\nLibSys: Library Management System")
        print("Search Book By: ")
        print("1. Book Title")
        print("2. Book Author")
        print("3. Book ISBN")
        print("4. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            title = input("Enter Book Title: ")
            query = session.query(Books).filter_by(title=title).all()
        elif choice == 2:
            author_name = input("Enter Book Author: ")
            query = session.query(Books).filter_by(author_name=author_name).all()
        elif choice == 3:
            isbn = input("Enter Book ISBN: ")
            query = session.query(Books).filter_by(isbn=isbn).all()

        self.print_query(query)
        session.close()

    def delete_book(self):
        session = Session()
        book_id = input("Enter Book Id to Delete: ")
        query = session.query(Books).get(book_id)
        if query is None:
            print("Book not found")
            return
        else:
            if not query.availability:
                print("Book is not available. Kindly retry once checked-in")
                session.close()
                return
            flag = input(f"Are you sure you want to delete {query.title} by {query.author_name} with ISBN number {query.isbn} (Y/N)")
            if flag.lower() == 'y':
                session.delete(query)
                session.commit()
                session.close()
                print("Book Deleted Successfully")
            else:
                session.close()
                return

    def edit_book(self):
        session = Session()
        book_id = int(input("Enter the book ID you want to edit: "))
        book = session.query(Books).get(book_id)
        
        if book is None:
            print("No book found with the given ID.")
            session.close()
            return

        print(f"Editing book: {book.title}")
        new_title = input("Enter new title (leave blank to keep current): ").strip()
        new_isbn = input("Enter new ISBN (leave blank to keep current): ").strip()
        new_language = input("Enter new language (leave blank to keep current): ").strip()
        new_author_name = input("Enter new author name (leave blank to keep current): ").strip()
        new_availability = input("Enter new availability (True/False, leave blank to keep current): ").strip()

        if new_title:
            book.title = new_title
        if new_isbn:
            book.isbn = new_isbn
        if new_language:
            book.language = new_language
        if new_author_name:
            book.author_name = new_author_name
        if new_availability.lower() in ['true', 'false']:
            book.availability = new_availability.lower() == 'true'

        session.commit()
        print("Book updated successfully.")
        session.close()

    def print_query(self, query):
        for book in query:
            print(f"Book ID: {book.id}, Title: {book.title}, Author: {book.author_name}, Availability: {book.availability}")
