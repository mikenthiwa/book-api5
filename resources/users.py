from flask_restplus import Namespace, Resource, fields, reqparse
from app.models import Users

api = Namespace('Users', description='Users related operations')

model_modify_info = api.model('modify', {'username': fields.String,
                                         'email': fields.String})


class User(Resource):
    req_data = reqparse.RequestParser()
    req_data.add_argument('username', type=str, required=False, location=['json'])
    req_data.add_argument('email', type=str, required=False, location=['json'])

    @api.expect(model_modify_info)
    def put(self, user_id):
        """Modify user info {username and email}"""
        args = self.req_data.parse_args(strict=True)
        username = args['username']
        email = args['email']

        if username:
            return Users.modify_username(user_id=user_id, username=username)

        elif email:
            return Users.modify_email(user_id=user_id, email=email)

        else:
            return {"msg": "At least one field is required"}

api.add_resource(User, '/auth/users/<int:user_id>')
