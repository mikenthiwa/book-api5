import unittest
import json
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.config_tests import ConfigTestCase


class RegisterEndPoint(ConfigTestCase):
    """This class represents the register test cases """

    def test_successful_sign_up(self):
        """Test API can register user successfully"""

        user = {"username": 'teddy', "email": 'teddy@gmail.com', "password": '123456789'}

        response = self.client().post('/api/v2/register', data=json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("user created", str(response.data))

    def test_missing_register_fields(self):
        """Test API for missing fields when registering"""

        user2 = {}
        response = self.client().post('/api/v2/register', data=json.dumps(user2), content_type='application/json')
        self.assertIn("No username provided Missing required parameter in the JSON body", str(response.data))
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
