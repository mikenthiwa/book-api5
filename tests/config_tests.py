import unittest
import json
import sys  # fix import errors
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import create_app
from app.models import Users


class ConfigTestCase(unittest.TestCase):
    """This class represents the books test case"""

    def setUp(self):
        """Define test variables and initialize app"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.book = {"title": "Lone Wolf",
                     "author": "David Archer",
                     "copies": 10}

        self.test_user = {"username": "test_user",
                          "email": "test_user@gmail.com",
                          "password": "123456789"}

        admin = Users()
        # admin.create_admin("admin", "admin@admin.com", "admin2018")

        # Register User
        self.client().post('/api/v1/register',
                           data=json.dumps(self.test_user),
                           content_type='application/json')



        user_response = self.client().post('/api/v1/login',
                                      data=json.dumps({"email": "test_user@gmail.com",
                                                       "password": "123456789"}),
                                      content_type='application/json')

        admin_response = self.client().post('/api/v1/login',
                                           data=json.dumps({"email": "admin@admin.com", "password": "admin2018"}),
                                           content_type='application/json')



        # Add book
        self.client().post('/api/v1/admin/books', data=json.dumps(self.book),
                           content_type='application/json')

        user_dict = json.loads(user_response.get_data(as_text=True))
        # self.admin_dict = json.loads(admin_response.get_data(as_text=True))

        user_token = user_dict['token']
        # admin_token = self.admin_dict['token']

        # self.user_header = {"Content-Type" : "application/json", "x-access-token" : user_token}
        # self.admin_header = {"Content-Type" : "application/json", "x-access-token" : admin_token}





if __name__ == '__main__':
    unittest.main()
