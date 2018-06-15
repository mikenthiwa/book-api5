#  test_book.py
import unittest
import json
import sys  # fix import errors
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.config_tests import ConfigTestCase


class BooksEndPoint(ConfigTestCase):
    """This class represents the books test case"""

    def test_get_all_books(self):
        """Test API can get all books"""
        response = self.client().get('/api/v1/books')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Lone Wolf", str(response.data))
        print(response.data)

    def test_get_a_book(self):
        """Test API can successfully get a book"""
        response = self.client().get('/api/v1/books/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Lone Wolf", str(response.data))


if __name__ == '__main__':
    unittest.main()