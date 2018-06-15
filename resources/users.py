from flask_restplus import Namespace, Resource, fields, reqparse
from app.models import Users, Books, users_db
from resources.auth import token_required

api = Namespace('signup and login', description='Users related operations')

# model for book
model_register = api.model('Register', {'username': fields.String,
                                        'email': fields.String,
                                        'password': fields.String})

model_login = api.model('Login', {'email': fields.String,
                                  'password': fields.String})

model_reset_password = api.model('Reset', {'password': fields.String})


user = Users()
book = Books()


class Register(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True, help="No username provided", location=['json'])

    parser.add_argument('email', required=True, help="No email provided", location=['json'])

    parser.add_argument('password', required=True, help="No password provided", location=['json'])

    @api.expect(model_register)
    def post(self):
        """Register user"""
        args = self.parser.parse_args()

        username = args['username']
        email = args['email']
        password = args['password']

        response = user.add_user(username=username, email=email, password=password)
        return response, 201


class Login(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', required=True, help='email required', location=['json'])

    parser.add_argument('password', required=True, help='password required', location=['json'])

    @api.expect(model_login)
    def post(self):
        """Login user"""
        args = self.parser.parse_args()
        email = args['email']
        password = args['password']

        for userid in users_db:
            return users_db



class BorrowedBook(Resource):
    """Authenticated users to borrow a book"""

    @token_required
    def get(self, book_id):
        response = book.get_a_book(book_id=book_id)
        return response


api.add_resource(Register, '/register', endpoint='register')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(BorrowedBook, '/auth/users/books/<int:book_id>')
