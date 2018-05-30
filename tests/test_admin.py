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
        self.assertIn("The Storm", str(response.data))

        """Test API if no book is provided"""
        response_1 = self.client().get('/api/v2/books/2')
        self.assertIn("book is not available", str(response_1.data))

    def test_modify_book_title(self):
        """Test API can modify book title"""
        title = {"title": "Harry Potter and Prisoner of Azkaban"}
        response = self.client().put('/api/v2/admin/books/1', data=json.dumps(title),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('book title modified', str(response.data))

    def test_modify_book_author(self):
        """Test API can modify book title"""
        author = {"author": "J.K Rowling"}
        response = self.client().put('/api/v2/admin/books/1', data=json.dumps(author),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('book author modified', str(response.data))

    def test_modify_book_copies(self):
        """Test API can modify book copies"""
        copies = {"copies": 50}
        response = self.client().put('/api/v2/admin/books/1', data=json.dumps(copies),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('book copies modified', str(response.data))

    def test_modify_book_info(self):
        """Test API can return reslt if no book info is provided"""
        book_info = {}
        response = self.client().put('/api/v2/admin/books/1', data=json.dumps(book_info),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("At least one field is required", str(response.data))

    def test_get_all_users(self):
        """Test API can get all users"""
        response = self.client().get('/api/v2/admin/users')
        self.assertEqual(response.status_code, 200)

    def test_get_a_user(self):
        """Test API can get a user"""
        response =  self.client().get('/api/v2/admin/users/1')
        self.assertEqual(response.status_code, 200)

    def test_reset_password(self):
        """Test API can reset password"""
        password = {"password": "987654321"}
        response = self.client().put('/api/v2/admin/users/1', data=json.dumps(password),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("password changed!", str(response.data))

    def test_promote_user(self):
        """Test API can promote user"""
        response = self.client().patch('/api/v2/admin/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("user has been promoted", str(response.data))

    def test_delete_user(self):
        """Test API can delete a user"""
        response = self.client().delete('/api/v2/admin/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("user deleted", str(response.data))

