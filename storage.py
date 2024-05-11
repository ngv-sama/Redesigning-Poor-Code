from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from models import Base, Users, Books, Checkout, Admins
import json


engine = create_engine("sqlite:///library.db")
Session=sessionmaker(bind=engine)


@event.listens_for(Admins.__table__, 'after_create')
def insert_initial_values(*args, **kwargs):
    session = Session()
    
    # Add default users
    users = [Users(name=f'User_{i}') for i in range(1, 6)]
    session.add_all(users)
    session.flush()  # Ensure IDs are assigned

    # Add default books
    books = [
        Books(title=f'Book_{i}', isbn=f'ISBN_{i}', language='English', author_name=f'Author_{i}')
        for i in range(1, 6)
    ]
    session.add_all(books)
    session.flush()

    # Add default checkouts
    checkouts = [
        Checkout(user_id=users[i].id, book_id=books[i].id)
        for i in range(5)
    ]
    session.add_all(checkouts)
    
    
    default_user = Users(name='Default')
    session.add(default_user)
    
    session.flush()

    default_admin=Admins(id=default_user.id, username='123456', password='123456')
    session.add(default_admin)
    session.commit()

    session.close()


def init_db():
    Base.metadata.create_all(engine)

def init_db_export():
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query data from each table
    data = {
        "Users": [dict(id=user.id, name=user.name) for user in session.query(Users).all()],
        "Books": [dict(id=book.id, title=book.title, isbn=book.isbn, language=book.language, author_id=book.author_id) for book in session.query(Books).all()],
        "Checkouts": [dict(id=checkout.id, user_id=checkout.user_id, book_id=checkout.book_id) for checkout in session.query(Checkout).all()],
        "Admins": [dict(id=admin.id, username=admin.username, password=admin.password, user_id=admin.user_id) for admin in session.query(Admins).all()]
    }

    session.close()

    # Write data to JSON file
    with open('library_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("Database export completed. Data is now stored in 'library_data.json'.")
