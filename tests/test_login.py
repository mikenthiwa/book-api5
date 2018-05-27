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
        response = self.client().post('/api/v2/login', data=json.dumps(user),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", str(response.data))

if __name__ == '__main__':
    unittest.main()
