from flask_restplus import Resource, Namespace
from app.models import Books

api = Namespace('Books', description='Books related operations')


class BookLists(Resource):
    """class contains GET method"""
    @staticmethod
    def get():
        """Get all books"""
        response = Books.get_all_books()
        return response


class Book(Resource):
    """class contains GET method"""
    @staticmethod
    def get(book_id):
        """Get one book"""
        response = Books.get_a_book(book_id=book_id)
        return response


api.add_resource(BookLists, '/books',
                 endpoint='books')

api.add_resource(Book, '/books/<int:book_id>')
