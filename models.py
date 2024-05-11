from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False)
    isbn = Column(String(256), nullable=False)
    language = Column(String(256), nullable=True)
    author_name = Column(String(256), nullable=True)
    availability = Column(Boolean, default=True)
    

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    admins = relationship("Admins", back_populates="user")
    checkouts = relationship("Checkout", back_populates="user")

class Admins(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True)
    username = Column(String(256), nullable=False)
    password = Column(String(256), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("Users", back_populates="admins")

class Checkout(Base):
    __tablename__ = 'checkout'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    user = relationship("Users", back_populates="checkouts")
    book = relationship("Books")