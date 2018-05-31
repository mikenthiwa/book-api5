from flask_restplus import Namespace, Resource, fields, reqparse
from app.models import Users, Books
from resources.auth import token_required, admin_required

api = Namespace('Admin', description='Admin related operations')

model_reset_password = api.model('Reset', {'password': fields.String})

model_book = api.model('Book', {'title': fields.String,
                                'author': fields.String,
                                'copies': fields.Integer})


class UserList(Resource):

    @staticmethod
    @admin_required
    def get():
        """Get all users"""
        response = Users.get_all_users()
        return response


class User(Resource):

    @staticmethod

    def get(user_id):
        """Get one users by id"""
        response = Users.get_a_user(id=user_id)
        return response


    def delete(self, user_id):
        """Delete user"""
        response = Users.delete_user(user_id=user_id)
        return response

    @api.expect(model_reset_password)

    def put(self, user_id):
        """Reset password"""
        parser = reqparse.RequestParser()
        # parser.add_argument('email', required=True, help="No email provided", location=['json'] )
        parser.add_argument('password', required=True, help="No password provided", location=['json'])
        args = parser.parse_args()
        response = Users.reset_password(id=user_id, password=args['password'])
        return response


    def patch(self, user_id):
        """Update user to admin"""
        response = Users.promote_user(user_id=user_id)
        return response


class BookLists(Resource):

    req_parser = reqparse.RequestParser()

    req_parser.add_argument('title', type=str, required=True,
                            help='book title is not provided', location=['json'])

    req_parser.add_argument('author', type=str, required=True,
                            help='book author is not provided', location=['json'])

    req_parser.add_argument('copies', type=int, required=True,
                            help='book copies is not provided', location=['json'])

    @api.expect(model_book)
    def post(self):
        """Add book"""
        args = self.req_parser.parse_args()
        title = args['title']
        author = args['author']
        copies = args['copies']
        response = Books.add_book(book_title=title, book_author=author,
                                  book_copies=copies)
        return response


class Book(Resource):
    req_parser = reqparse.RequestParser()
    req_parser.add_argument('title', type=str, required=False, location=['json'])

    req_parser.add_argument('author', type=str, required=False, location=['json'])

    req_parser.add_argument('copies', type=int, required=False, location=['json'])


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
            response = Books.modify_book_title(book_id=book_id, title=title)
            return response

        elif author:
            response = Books.modify_book_author(book_id=book_id, author=author)
            return response

        elif copies:
            response = Books.modify_book_copies(book_id=book_id, copies=copies)
            return response

        else:
            return {"msg": "At least one field is required"}


    def delete(self, book_id):
        """Delete book"""
        response = Books.delete_book(book_id=book_id)
        return response


api.add_resource(UserList, '/admin/users', endpoint='users')
api.add_resource(User, '/admin/users/<int:user_id>')
api.add_resource(BookLists, '/admin/books', endpoint='library')
api.add_resource(Book, '/admin/books/<int:book_id>')
