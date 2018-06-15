from flask import jsonify, request, make_response
from functools import wraps
import jwt
from instance.config import Config

def token_required(f):
    """Checks for authenticated users with valid token in the header"""

    @wraps(f)
    def decorated(*args, **kwargs):
        """validate token provided"""
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if token is None:
            return make_response(jsonify({
                "message" : "kindly provide a valid token in the header"}), 401)

        try:
            data = jwt.decode(token, Config.SECRET) # pylint: disable=W0612
        except:
            return make_response(jsonify({
                "message" : "kindly provide a valid token in the header"}), 401)
        return f(*args, **kwargs)

    return decorated

def admin_required(f):
    """Checks for authenticated admins with valid token in the header"""

    @wraps(f)
    def decorated(*args, **kwargs):
        """validate token provided and ensures the user is an admin"""
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if token is None:
            return make_response(jsonify({
                "message" : "token missing"}), 401)

        try:
            data = jwt.decode(token, Config.SECRET)
            admin = data['admin']
        except:
            return make_response(jsonify({
                "message" : "kindly provide a valid token in the header"}), 401)

        if not admin:
            return make_response(jsonify({
                "message" : "you are not authorized to perform this function as a non-admin user"}), 401)

        return f(*args, **kwargs)

    return decorated