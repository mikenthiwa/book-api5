#  test_login.py
import unittest
import json
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.config_tests import ConfigTestCase


class LoginEndPoint(ConfigTestCase):
    """This class represents the login test cases """

    def test_successful_login(self):
        """Test API can login user successfully"""

        admin = {"email": "admin@admin.com", "password": "admin2018"}
        user = {"email": "mike.nthiwa@gmail.com", "password": "123456789"}

        admin_response = self.client().post('/api/v2/login', data=json.dumps(admin), content_type='application/json')
        self.assertEqual(admin_response.status_code, 200)
        self.assertIn("token", str(admin_response.data))

        user_response = self.client().post('/api/v2/login', data=json.dumps(user), content_type='application/json')
        self.assertEqual(admin_response.status_code, 200)
        self.assertIn("token", str(user_response.data))

    def test_invalid_email_login(self):
        """Test API for invalid email"""

        user = {"email": "test2@gmail.com", "password": "123456789"}
        response = self.client().post('/api/v2/login', data=json.dumps(user), content_type='application/json')
        self.assertIn("email is not available", str(response.data))
        self.assertEqual(response.status_code, 401)

    def test_invalid_password(self):
        """Test API for invalid password"""

        user = {"email": "mike.nthiwa@gmail.com", "password": "123456"}
        response = self.client().post('/api/v2/login', data=json.dumps(user), content_type='application/json')
        self.assertIn("password do not match", str(response.data))
        self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()
