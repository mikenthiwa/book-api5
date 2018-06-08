import unittest
import json
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.config_tests import ConfigTestCase


class UserEndPoint(ConfigTestCase):
    """This class represents the user cases """

    def test_modify_email(self):
        """Test API can modify email"""
        email = {"email": "mike.nthiwa@yahoo.com"}
        response = self.client().put('api/v2/auth/users/2', data=json.dumps(email),
                                     content_type='application/json', headers=self.user_header)
        self.assertIn("email changed", str(response.data))
        self.assertEqual(response.status_code, 200)

        """Test if user is not available"""
        response_2 = self.client().put('/api/v2/auth/users/5', data=json.dumps(email),
                                       content_type='application/json', headers=self.user_header)
        self.assertIn("user does not exist", str(response_2.data))

    def test_modify_username(self):
        """Test API can modify username"""
        username = {"username": "mikenthiwa"}
        response = self.client().put('api/v2/auth/users/1', data=json.dumps(username),
                                     content_type='application/json', headers=self.user_header)
        self.assertIn("username changed", str(response.data))
        self.assertEqual(response.status_code, 200)

        """Test if user is not available"""
        response_2 = self.client().put('/api/v2/auth/users/5', data=json.dumps(username),
                                       content_type='application/json', headers=self.user_header)
        self.assertIn("user does not exist", str(response_2.data))

    def test_no_value_provided_when_modifying_user(self):
        data = {}
        response = self.client().put('api/v2/auth/users/1', data=json.dumps(data),
                                     content_type='application/json', headers=self.user_header)
        self.assertIn("At least one field is required", str(response.data))
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
