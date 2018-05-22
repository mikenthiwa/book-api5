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
        """Test API can get post a books (POST request)"""
        response = self.client().post('/api/v1/admin/books', data=json.dumps(self.book),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("book added", str(response.data))

    def test_modify_book_title(self):
        response = self.client().put('/api/v1/admin/books/1', data=json.dumps(self.title),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Title modified to", str(response.data))

    def test_modify_book_author(self):
        author = {"author": "Joanne K Rowling"}
        response = self.client().put('/api/v1/admin/books/1', data=json.dumps(author),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("author modified to", str(response.data))

    def test_modify_book_copies(self):
        copies = {"copies": 20}
        response = self.client().put('/api/v1/admin/books/1', data=json.dumps(copies),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Copies modified to", str(response.data))

    def test_empty_field_modify_book_info(self):
        data = {}
        response = self.client().put('/api/v1/admin/books/1', data=json.dumps(data),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("At least one field is required", str(response.data))

if __name__ == '__main__':
    unittest.main()