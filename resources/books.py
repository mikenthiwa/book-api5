from flask_restplus import Resource, Namespace, fields, reqparse
from app.models import Books

api = Namespace('Books', description='Books related operations')

# model for book
model_book = api.model('Book', {'title': fields.String,
                                'author': fields.String,
                                'copies': fields.Integer})

book = Books()


class BookLists(Resource):

    req_parser = reqparse.RequestParser()

    req_parser.add_argument('title', type=str, required=True,
                            help='book title is not provided', location=['json'])

    req_parser.add_argument('author', type=str, required=True,
                            help='book author is not provided', location=['json'])

    req_parser.add_argument('copies', type=int, required=True,
                            help='book copies is not provided', location=['json'])


    # @api.marshal_with(envelop='Books')
    def get(self):
        res = book.get_all_books()
        return res

    @api.expect(model_book)
    def post(self):

        args = self.req_parser.parse_args()
        title = args['title']
        author = args['author']
        copies = args['copies']
        res = book.add_book(book_title=title, book_author=author, book_copies=copies)
        return res

class Book(Resource):
    req_parser = reqparse.RequestParser()
    req_parser.add_argument('title', type=str, required=False, location=['json'])

    req_parser.add_argument('author', type=str, required=False, location=['json'])

    req_parser.add_argument('copies', type=int, required=False, location=['json'])

    def get(self, book_id):

        response = book.get_a_book(book_id=book_id)
        return response


    @api.expect(model_book)
    def put(self, book_id):
        """ modify book information
                endpoint = /api/v1/books/<int:book_id>
                method == PUT"""
        args = self.req_parser.parse_args(strict=True)
        title = args['title']
        author = args['author']
        copies = args['copies']

        if title:
            title_response = book.modify_book_title(book_id=book_id, title=title)
            return title_response

        elif author:
            author_response = book.modify_book_author(book_id=book_id, author=author)
            return author_response

        elif copies:
            copies_response = book.modify_book_copies(book_id=book_id, copies=copies)
            return copies_response

        else:
            return {"At least one field is required"}
api.add_resource(BookLists, '/books',
                 endpoint='books')

api.add_resource(Book, '/books/<int:book_id>')