import unittest
import sys  # fix import errors
import os
import json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import db, create_app


class ConfigTestCase(unittest.TestCase):
    """This class represents the books test case"""

    def setUp(self):
        """Define test variables and initialize app"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.book = {"title": "The Storm", "author": "Blake Banner", "copies": 8}
        self.users = {"username": "mike.nthiwa", "email": "mike.nthiwa@gmail.com", "password": "123456789"}
        self.admin = {"username": "admin", "email": "admin@gmail.com", "password": "123456789"}

        self.user_cred = {"email": "mike.nthiwa@gmail.com",
                          "password": "123456789"}

        self.admin_cred = {"email": "admin@gmail.com",
                           "password": "123456789"}
        # binds the app to the current context
        with self.app.app_context():
            # create all tables

            db.create_all()

            self.client().post('/api/v2/admin/books',
                               data=json.dumps(self.book),
                               content_type='application/json')

            self.client().post('/api/v2/register',
                               data=json.dumps(self.users),
                               content_type='application/json')

            self.client().post('/api/v2/register',
                               data=json.dumps(self.admin),
                               content_type='application/json')

            user_response = self.client().post('/api/v2/login', data=json.dumps(self.user_cred),
                                               content_type='application/json')
            admin_response = self.client().post('/api/v2/login', data=json.dumps(self.admin_cred),
                                               content_type='application/json')

            user_token_dict = json.loads(user_response.get_data(as_text=True))
            admin_token_dict = json.loads(admin_response.get_data(as_text=True))

            user_token = user_token_dict["token"]
            admin_token = admin_token_dict['token']

            self.user_header = {"Content-Type": "application/json", "x-access-token": user_token}
            self.admin_header = {"Content-Type": "application/json", "x-access-token": admin_token}


    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()
