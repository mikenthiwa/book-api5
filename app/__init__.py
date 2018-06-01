from flask import Flask
from flask_restplus import Api
from app.models import db
from instance.config import app_config
from resources.books import api as book
from resources.reg_login import api as user
from resources.admin import api as admin
from resources.users import api as users


def create_app(config_name):

    # Expect token in api_doc
    authorizations = {'apikey': {'type': 'apiKey',
                                 'in': 'header',
                                 'name': 'x-access-token'}}

    # Create flask app
    app = Flask(__name__, instance_relative_config=True)
    api = Api(app=app,
              authorizations=authorizations,
              title='Book-API',
              version='2.0',
              description='Hello-Books is a simple api that helps manage a library and its processes'
                          ' like stocking,tracking and renting books.\n With this application users are'
                          ' able to find and rent books. The application also has an admin section where'
                          ' the admin\n can do things like add books, delete books')

    # Enable swagger editor
    app.config['SWAGGER_UI_JSONEDITOR'] = True

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.url_map.strict_slashes = False

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # initialise db
    db.init_app(app)

    #  Register application
    api.add_namespace(user, path='/api/v2')
    api.add_namespace(book, path='/api/v2')
    api.add_namespace(admin, path='/api/v2')
    api.add_namespace(users, path='/api/v2')

    return app
