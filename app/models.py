import os
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

class Books:
    books = {1: {"Title": "Harry Potter", "Author": "J.K.Rowling", "Copies": 3},
             2: {"Title": "The whistler", "Author": "John Grisham", "Copies": 3}}

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
    users = {1: {"username": "mike.nthiwa","email": "mike.nthiwa@gmail.com",
                 "password": "123456789", "admin": False},
             2: {"username": "reg.nthiwa", "email": "reg.nthiwa@gmail.com",
                 "password": "123456789", "admin": False},
             3: {"username": "emma.nthiwa", "email": "emma.nthiwa@gmail.com",
                 "password": "123456789", "admin": False}}


    def get_all_users(self):
        response = self.users
        return response

    def get_a_user(self, user_id):
        response = self.users.get(user_id)
        return response

    def login_user(self, email, password):
        for user_id in self.users:
            if self.users[user_id]['email'] != email:

                return {'msg': 'invalid email'}
            if self.users[user_id]['password'] != password:
                return {"msg": 'invalid password'}
            user = self.users.get(user_id)
            email = user['email']
            token = jwt.encode(
                {'email': email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                os.getenv("SECRET"))
            return ({'token': token.decode('UTF-8')})


    def add_user(self, username, email, password, admin=False):
        new_id = len(self.users) + 1
        hashed_password = generate_password_hash(password=password, method='sha256')
        self.users[new_id] = [{"username": username, "email": email,
                               "password": hashed_password, "admin": admin}]
        return {"msg": 'user added'}

    def delete_user(self, user_id):
        del self.users[user_id]
        return {"msg": 'user deleted'}

    def modify_username(self, user_id, username):
        user = self.users.get(user_id)
        user['username'] = username
        return {"msg": 'username changed'}

    def modify_email(self, user_id, email):
        user = self.users.get(user_id)
        user['email'] = email
        return {"msg": 'email changed'}

    def promote_user(self, user_id):
        user = self.users.get(user_id)
        user['admin'] = True
        return {"msg": 'user is admin!'}

    def reset_password(self, user_id, password):
        user = self.users.get(user_id)
        user['password'] = password
        return {"msg": "password changed!"}
