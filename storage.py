from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from models import Base, Users, Books, Checkout, Admins


engine = create_engine("sqlite:///library.db")
Session=sessionmaker(bind=engine)


@event.listens_for(Admins.__table__, 'after_create')
def insert_initial_values(*args, **kwargs):
    session = Session()
    
    default_user = Users(name='Default')
    session.add(default_user)
    
    session.flush()

    default_admin=Admins(id=default_user.id, username='123456', password='123456')
    session.add(default_admin)
    session.commit()

    session.close()


def init_db():
    Base.metadata.create_all(engine)

