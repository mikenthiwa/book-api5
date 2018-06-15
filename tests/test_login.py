import unittest
import json
import sys  # fix import errors
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.config_tests import ConfigTestCase

class RegisterEndPoint(ConfigTestCase):
    """This class represents the login user test case"""

    def test_successful_login(self):
        """Test API can login user"""

        response = self.client().post('/api/v1/login', data=json.dumps(self.test_user),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", str(response.data))


if __name__ == '__main__':
    unittest.main()