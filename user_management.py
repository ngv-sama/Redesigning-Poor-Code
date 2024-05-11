from storage import Session, init_db
from models import Users, Books, Checkout, Admins


def add_new_user():
    session=Session()
    name = input("Enter Name of New User: ")
    new_user=Users(name=name)
    session.add(new_user)
    session.commit()
    session.close()


def add_new_admin():
    session=Session()
    username = input("Enter Username of New Admin: ")
    password=input("Enter Username of New Admin: ")
    user_id=input("Enter User Id of New Admin: ")
    new_admin=Admins(username=username, password=password, user_id=user_id)
    session.add(new_admin)
    session.commit()
    session.close()
