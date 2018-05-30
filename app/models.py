import os
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

db = SQLAlchemy()

class Books(db.Model):
    """This class represents the books table."""
    __tablename__ = 'books'

    book_id = db.Column(db.Integer, nullable=False, primary_key=True)
    book_title = db.Column(db.String(80), unique=True, nullable=False)
    book_author = db.Column(db.String(50), unique=True, nullable=False)
    book_copies = db.Column(db.Integer, nullable=False)

    @staticmethod
    def get_all_books():
        """Method to get all books in db"""
        books = Books.query.all()
        output = []
        for book in books:
            book_data = {}
            book_data['book_id'] = book.book_id
            book_data['book_title'] = book.book_title
            book_data['book_author'] = book.book_author
            book_data['book_copies'] = book.book_copies
            output.append(book_data)

        return {"book": output}

    @staticmethod
    def get_a_book(book_id):
        """Method to get one book in db"""
        book = Books.query.filter_by(book_id=book_id).first()

        if book is None:
            return {"msg": "book is not available"}

        return {"book id": book.book_id, "book_title": book.book_title, "book_author": book.book_author,
                        "book_copies": book.book_copies}

    @classmethod
    def add_book(cls, book_title, book_author, book_copies):
        """Method to get add a books in db"""
        new_book = cls(book_title=book_title, book_author=book_author, book_copies=book_copies)
        db.session.add(new_book)
        db.session.commit()
        return {"msg": "book created"}

    @staticmethod
    def delete_book(book_id):
        """Method to delete book in db"""
        book = Books.query.get(book_id)
        db.session.delete(book)
        db.session.commit()
        return {"msg": "book successfully deleted"}

    @staticmethod
    def modify_book_title(book_id, title):
        """Method to modify book title in db"""
        book = Books.query.get(book_id)

        if book is None:
            return {"msg": "book is not available"}

        if title:
            book.book_title = title
            db.session.commit()
            return {"msg": 'book title modified'}

    @staticmethod
    def modify_book_author(book_id, author):
        """Method to modify book author in db"""
        book = Books.query.get(book_id)

        if book is None:
            return {"msg": "book is not available"}

        if author:
            book.book_title = author
            db.session.commit()
            return {"msg": 'book author modified'}

    @staticmethod
    def modify_book_copies(book_id, copies):
        """Method to modify book copies in db"""
        book = Books.query.get(book_id)

        if book is None:
            return {"msg": "book is not available"}

        book.book_copies = copies
        db.session.commit()
        return {"msg": 'book copies modified'}


class Users(db.Model):
    """This class represents User table"""
    id = db.Column('id', db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(80))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)

    @staticmethod
    def get_all_users():
        """Get all users in db"""
        users = Users.query.all()
        output = []
        for user in users:
            user_data = {}
            user_data['public_id'] = user.public_id
            user_data['username'] = user.username
            user_data['email'] = user.email
            user_data['password'] = user.password
            output.append(user_data)

        return {"Users": output}

    @staticmethod
    def get_a_user(id):
        user = Users.query.filter_by(id=id).first()

        if user is None:
            return {'msg': 'user does not exist'}

        return {"username": user.username, "public_id": user.id, "admin": user.admin, "password": user.password}

    @staticmethod
    def login_user(email, password):
        user = Users.query.filter_by(email=email).first()
        # no username provide
        if not user:
            return {"msg": "email is not available"}

        # check password
        if check_password_hash(user.password, password):
            token = jwt.encode(
                {'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                os.getenv("SECRET"))
            return {'token': token.decode('UTF-8')}
        return {"msg": "password do not match"}

    @classmethod
    def add_user(cls, username, email, password, admin=False):
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = cls(public_id=str(uuid.uuid4()), username=username, email=email, password=hashed_password,
                       admin=admin)
        db.session.add(new_user)
        db.session.commit()
        return {"msg": "user crested"}

    @staticmethod
    def delete_user(user_id):
        user = Users.query.filter_by(id=user_id).first()
        if user is None:
            return {'msg': 'user does not exist'}
        db.session.delete(user)
        db.session.commit()
        return {"msg": "user deleted"}

    @staticmethod
    def modify_username(public_id, username):
        user = Users.query.filter_by(public_id=public_id).first()
        if user is None:
            return {'msg': 'user does not exist'}
        user.username = username
        db.session.commit()
        return {"msg": 'username changed'}

    def modify_email(self, public_id, email):
        user = Users.query.filter_by(public_id=public_id).first()
        if user is None:
            return {'msg': 'user does not exist'}
        user.email = email
        db.session.commit()
        return {"msg": 'email changed'}

    @staticmethod
    def promote_user(user_id):
        user = Users.query.filter_by(id=user_id).first()

        if user is None:
            return {'msg': 'user does not exist'}

        # update user to admin
        user.admin = True
        db.session.commit()

        return {"msg": "user has been promoted"}

    @staticmethod
    def reset_password(id, password):
        user = Users.query.filter_by(id=id).first()
        if user is None:
            return {'msg': 'user does not exist'}
        user.password = password
        db.session.commit()
        return {"msg": "password changed!"}
