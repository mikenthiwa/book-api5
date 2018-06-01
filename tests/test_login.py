#  test_login.py
import unittest
import json
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.config_tests import ConfigTestCase


class LoginEndPoint(ConfigTestCase):
    """This class represents the login test cases """

    def test_login(self):
        """Test API can login user"""
        user = {"email": "mike.nthiwa@gmail.com", "password": "123456789"}
        user_1 = {"email": "reg.nthiwa@gmail.com", "password": "123456789"}
        user_2 = {"email": "mike.nthiwa@gmail.com", "password": "123456"}

        response = self.client().post('/api/v2/login', data=json.dumps(user),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", str(response.data))

        """Test API can detect email that is unavailable"""
        response_1 = self.client().post('/api/v2/login', data=json.dumps(user_1),
                                        content_type='application/json')
        self.assertIn("email is not available", str(response_1.data))
        self.assertEqual(response_1.status_code, 401)

        """Test API can detect wrong password"""
        response_2 = self.client().post('/api/v2/login', data=json.dumps(user_2),
                                      content_type='application/json')
        self.assertIn("password do not match", str(response_2.data))
        self.assertEqual(response_2.status_code, 401)



if __name__ == '__main__':
    unittest.main()