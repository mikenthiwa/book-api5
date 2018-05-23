#  test_login.py
import unittest
import json
import sys  # fix import errors
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.config_tests import ConfigTestCase

class RegisterEndPoint(ConfigTestCase):
    """This class represents the register user test case"""

    def test_sign_up(self):
        """Test API can get register a user (POST request)"""
        response = self.client().post('/api/v1/register', data=json.dumps(self.user),
                                      content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertIn("user added", str(response.data))

    def test_login(self):
        """Test registered user can login."""
        user = {"email": "mike.nthiwa@gmail.com",
                "password": "123456789"}
        response = self.client().post('/api/v1/login', data=json.dumps(user),
                                      content_type='application/json')

        self.assertEqual(response.status_code, 200)

    def test_none_registered_user_login(self):
        """Test registered user can login."""
        user = {"email": "brian.mutua@gmail.com",
                "password": "123456789"}
        response = self.client().post('/api/v1/login', data=json.dumps(user),
                                      content_type='application/json')

        self.assertIn("invalid email", str(response.data))




if __name__ == '__main__':
    unittest.main()