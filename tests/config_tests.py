import unittest
import sys  # fix import errors
import os
from werkzeug.security import generate_password_hash
import json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import db, create_app
from app.models import Users, Books


class ConfigTestCase(unittest.TestCase):
    """This class represents the books test case"""

    def setUp(self):
        """Define test variables and initialize app"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.book = {"title": "The Storm", "author": "Blake Banner", "copies": 8}


        # binds the app to the current context
        with self.app.app_context():
            # create all tables

            db.create_all()

            # create test admin user

            test_admin = Users(email="admin@admin.com", password=generate_password_hash("admin2018", method='sha256'), admin=True)
            test_user = Users(email="mike.nthiwa@gmail.com", password=generate_password_hash("123456789", method='sha256'))
            test_book = Books(book_title="The Storm", book_author="Blake Banner", book_copies=8)
            db.session.add(test_admin)
            db.session.add(test_user)
            db.session.add(test_book)
            db.session.commit()

            admin = {"email": "admin@admin.com", "password": "admin2018"}
            user = {"email": "mike.nthiwa@gmail.com", "password": "123456789"}

            # Login users
            user_response = self.client().post('/api/v2/login', data=json.dumps(user), content_type='application/json')
            admin_response = self.client().post('/api/v2/login', data=json.dumps(admin), content_type='application/json')


            admin_token_dict = json.loads(admin_response.get_data(as_text=True))
            user_token_dict = json.loads(user_response.get_data(as_text=True))

            admin_token = admin_token_dict["token"]
            user_token = user_token_dict["token"]

            self.user_header = {"Content-Type": "application/json", "x-access-token": user_token}
            self.admin_header = {"Content-Type": "application/json", "x-access-token": admin_token}



    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()

if __name__ == '__main__':
    unittest.main()