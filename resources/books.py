from flask_restplus import Resource, Namespace
from app.models import Books

api = Namespace('Books', description='Books related operations')

book = Books()


class BookLists(Resource):

    def get(self):
        """Get all books"""
        pass



class Book(Resource):
    def get(self, book_id):
        """Get one book"""
        pass



api.add_resource(BookLists, '/books',
                 endpoint='books')

api.add_resource(Book, '/books/<int:book_id>')
