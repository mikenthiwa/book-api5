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