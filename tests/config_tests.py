import unittest
import json
import sys  # fix import errors
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import create_app


class ConfigTestCase(unittest.TestCase):
    """This class represents the books test case"""

    def setUp(self):
        """Define test variables and initialize app"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.book = {"title": "Harry Potter",
                     "author": "J.K Rowling",
                     "copies": 10}

        self.user = {"username": "chris.mutua",
                     "email": "chris.mutua@gmail.com",
                     "password": "123456789"}

        user_response = self.client().post('/api/v1/login',
                                      data=json.dumps({"email": "mike.nthiwa@gmail.com",
                                                       "password": "123456789"}),
                                      content_type='application/json')

        user_dict = json.loads(user_response.get_data(as_text=True))
        user_token = user_dict['token']
        self.user_header = {"Content-Type" : "application/json",
                            "x-access-token" : user_token}



if __name__ == '__main__':
    unittest.main()
