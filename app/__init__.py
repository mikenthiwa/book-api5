from flask import Flask
from flask_restplus import Api
from instance.config import app_config
from resources.books import api as book
from resources.users import api as users
from resources.admin import api as admin
from werkzeug.contrib.fixers import ProxyFix


def create_app(config_name):
app.wsgi_app = ProxyFix(app.wsgi_app)
    
    api = Api(title='Book-API',
              version='1.0',
              description='Hello-Books is a simple api that helps manage a library and its processes'
                          ' like stocking,tracking and renting books.\n With this application users are'
                          ' able to find and rent books. The application also has an admin section where'
                          ' the admin\n can do things like add books, delete books')

    # Create flask app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.url_map.strict_slashes = False

    # Enable swagger editor
    app.config['SWAGGER_UI_JSONEDITOR'] = True

    #  Register application
    api.add_namespace(users, path='/api/v1')
    api.add_namespace(book, path='/api/v1')
    api.add_namespace(admin, path='/api/v1')

    api.init_app(app=app)



    return app
