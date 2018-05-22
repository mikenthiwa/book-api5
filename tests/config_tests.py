import unittest
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

if __name__ == '__main__':
    unittest.main()