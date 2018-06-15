#  test_login.py
import unittest
import json
import sys  # fix import errors
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.config_tests import ConfigTestCase

class RegisterEndPoint(ConfigTestCase):
    """This class represents the register user test case"""

    def test_successful_sign_up(self):
        """Test API can create user"""

        user = {"username": 'teddy', "email": 'teddy@gmail.com', "password": '123456789'}
        response = self.client().post('/api/v1/register', data=json.dumps(user), content_type='application/json')
        self.assertIn("user added", str(response.data))
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
