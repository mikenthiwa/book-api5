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
        self.book = {"title": "Harry Potter",
                    "author": "J.K Rowling",
                    "copies": 10}

        self.title = {"title": "Harry Potter and Chamber of Secrets"}

if __name__ == '__main__':
    unittest.main()