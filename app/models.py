import os
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

users_db = {1: {"username": "mike", "email": "mike@gmail.com", "password":"123"},
            2: {"username": "reg", "email": "reg@gmail.com", "password": "123"}}


class Books:
    books = {}

    def get_all_books(self):
        response = self.books
        return response

    def get_a_book(self, book_id):
        response = self.books.get(book_id)
        return response

    def add_book(self, book_title, book_author, book_copies):
        new_id = len(self.books) + 1
        self.books[new_id] = [{"Title": book_title, "Author": book_author, "Copies": book_copies}]
        return {"msg": 'book added'}

    def delete_book(self, book_id):
        del self.books[book_id]
        return {"msg": 'book deleted'}

    def modify_book_title(self, book_id, title):
        book = self.books.get(book_id)
        new_title = book['Title'] = title
        return {"msg": 'Title modified to: {}'.format(new_title)}


    def modify_book_author(self, book_id, author):
        book = self.books.get(book_id)
        new_author = book['Author'] = author
        return {"msg": 'author modified to: {}'.format(new_author)}

    def modify_book_copies(self, book_id, copies):
        book = self.books.get(book_id)
        copy = book['Copies'] = copies
        return {"msg": 'Copies modified to: {}'.format(copy)}


class Users:

    def get_all_users(self):
        response = users_db
        return response

    def get_a_user(self, user_id):
        response = users_db.get(user_id)
        return response


    def add_user(self, username, email, password, admin=False):
        new_id = len(users_db) + 1
        hashed_password = generate_password_hash(password=password, method='sha256')
        users_db[new_id] = {"username": username, "email": email,
                               "password": hashed_password, "admin": admin}

        return {"msg": 'user added'}


    def delete_user(self, user_id):
        del users_db[user_id]
        return {"msg": 'user deleted'}

    def modify_username(self, user_id, username):
        user = users_db.get(user_id)
        user['username'] = username
        return {"msg": 'username changed'}

    def modify_email(self, user_id, email):
        user = users_db.get(user_id)
        user['email'] = email
        return {"msg": 'email changed'}

    def promote_user(self, user_id):
        user = users_db.get(user_id)
        user['admin'] = True
        return {"msg": 'user is admin!'}

    def reset_password(self, user_id, password):
        user = users_db.get(user_id)
        user['password'] = password
        return {"msg": "password changed!"}


    def create_admin(self, username, email, password, admin=True):
        new_id = len(users_db) + 1
        hashed_password = generate_password_hash(password=password, method='sha256')
        users_db[str(new_id)] = {"username": username, "email": email, "password": hashed_password, "admin": admin}
        return {"msg": "admin created"}

