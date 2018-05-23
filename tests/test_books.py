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
        """Test API can get all books (POST request)"""
        response = self.client().get('/api/v1/books')
        self.assertEqual(response.status_code, 200)
        # self.assertIn("Harry Potter", str(response.data))

    def test_get_one_book(self):
        """Test API can get a book"""
        response = self.client().get('/api/v1/books/1')
        self.assertEqual(response.status_code, 200)

    def test_auth_user_borrows_book(self):
        """Test API can authenticated users borrow book"""
        response = self.client().get('api/v1/auth/users/books/1',
                                     headers=self.user_header)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()