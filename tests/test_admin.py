#  test_admin.py
import unittest
import json
import sys  # fix import errors
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.config_tests import ConfigTestCase


class AdminEndPoint(ConfigTestCase):
    """This class represents the Admin test case"""

    def test_add_book(self):
        """Test API can create a book (POST request)"""
        book = {"title": "Harry Potter and Prisoner of Azkaban", "author": "J.K Rowling", "copies": 25}
        response = self.client().post('/api/v1/admin/books', data=json.dumps(book), content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertIn("book added", str(response.data))



if __name__ == '__main__':
    unittest.main()