from flask_restplus import Namespace, Resource, fields, reqparse
from app.models import Users, Books

api = Namespace('Admin', description='Admin related operations')

model_reset_password = api.model('Reset', {'password': fields.String})

model_book = api.model('Book', {'title': fields.String,
                                'author': fields.String,
                                'copies': fields.Integer})

user = Users()
book = Books()


class UserList(Resource):
    @staticmethod
    def get():
        """Get all users"""
        response = user.get_all_users()
        return response


class User(Resource):
    @staticmethod
    def get(user_id):
        """Get one users by id"""
        pass


    def delete(self, user_id):
        """Delete user"""
        pass

    @api.expect(model_reset_password)
    def put(self, user_id):
        """Reset password"""
        parser = reqparse.RequestParser()
        # parser.add_argument('email', required=True, help="No email provided", location=['json'] )
        parser.add_argument('password', required=True, help="No password provided", location=['json'])
        pass

    def patch(self, user_id):
        """Update user to admin"""
        pass




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
        pass

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
            pass

        elif author:
            pass

        elif copies:
            pass

        else:
            return {"msg": "At least one field is required"}


    

api.add_resource(UserList, '/auth/users', endpoint='users')
api.add_resource(User, '/auth/users/<int:user_id>')
api.add_resource(BookLists, '/admin/books', endpoint='library')
api.add_resource(Book, '/admin/books/<int:book_id>')

