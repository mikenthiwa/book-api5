#  test_admin.py
import unittest
import json
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.config_tests import ConfigTestCase


class AdminEndPoint(ConfigTestCase):
    """This class represents the books test case"""

    def test_add_book(self):
        """Test API can create a book (POST request)"""
        book = {"title": "Harry Potter and Prisoner of Azkaban",
                "author": "J.K Rowling", "copies": 25}
        response = self.client().post('/api/v2/admin/books', data=json.dumps(book),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("book created", str(response.data))

    def test_get_all_books(self):
        """Test API can get all books in db"""
        response = self.client().get('/api/v2/books')
        self.assertEqual(response.status_code, 200)
        self.assertIn("The Storm", str(response.data))

    def test_get_book(self):
        """Test API can get one book"""
        response =  self.client().get('/api/v2/books/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.data)