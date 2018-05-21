from flask_restplus import Namespace, Resource, fields, reqparse
from app.models import Users

api = Namespace('Admin', description='Admin related operations')

model_reset_password = api.model('Reset', {'password': fields.String})

user = Users()


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
        response = user.get_a_user(user_id=user_id)
        return response

    @staticmethod
    def delete(user_id):
        """Delete user"""
        response = user.delete_user(user_id=user_id)
        return response

    @api.expect(model_reset_password)
    def put(self, user_id):
        """Reset password"""
        parser = reqparse.RequestParser()
        # parser.add_argument('email', required=True, help="No email provided", location=['json'] )
        parser.add_argument('password', required=True, help="No password provided", location=['json'])
        response = user.reset_password(user_id=user_id, password=api.payload['password'])
        return response


api.add_resource(UserList, '/auth/users', endpoint='users')
api.add_resource(User, '/auth/users/<int:user_id>')
