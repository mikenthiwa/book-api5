# manage.py

import os
import sys
from flask_script import Manager, prompt, prompt_pass # class for handling a set of commands
from flask_migrate import Migrate, MigrateCommand
from app import db, create_app
import re
from app.models import Users

app = create_app(config_name=os.getenv('APP_SETTINGS'))
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
@manager.command
def createsuperuser():
    """Create a superuser, requires username, email and password."""

    username = prompt('superuser username')

    email = prompt('superuser email')
    confirm_email = prompt('confirm superuser email')

    if not EMAIL_REGEX.match(email):
        sys.exit('\n kindly provide a valid email address')

    if not email == confirm_email:
        sys.exit('\n kindly ensure that email and confirm email are identical')

    password = prompt_pass('superuser password')
    confirm_password = prompt_pass('confirm superuser password')

    if not password == confirm_password:
        sys.exit('\n kindly ensure that password and confirm password are identical')

    Users.create_admin(username=username, email=email, password=password)


if __name__ == '__main__':
    manager.run()