#  test_admin.py
import unittest
import json
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.config_tests import ConfigTestCase


class AdminEndPoint(ConfigTestCase):
    """This class represents the Admin test case"""

    def test_add_book(self):
        """Test API can create a book (POST request)"""
        book = {"title": "Harry Potter and Prisoner of Azkaban", "author": "J.K Rowling", "copies": 25}
        response = self.client().post('/api/v2/admin/books', data=json.dumps(book),
                                      content_type='application/json', headers=self.admin_header)
        self.assertEqual(response.status_code, 200)
        self.assertIn("book created", str(response.data))

    def test_get_all_books(self):
        """Test API can get all books in db"""
        response = self.client().get('/api/v2/books')
        self.assertEqual(response.status_code, 200)
        self.assertIn("The Storm", str(response.data))

    def test_get_book(self):
        """Test API can get one book"""
        response = self.client().get('/api/v2/books/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("The Storm", str(response.data))

        """Test API if no book is provided"""
        response_1 = self.client().get('/api/v2/books/2')
        self.assertIn("book is not available", str(response_1.data))

    def test_modify_book_title(self):
        """Test API can modify book title"""
        title = {"title": "Harry Potter and Prisoner of Azkaban"}
        response = self.client().put('/api/v2/admin/books/1', data=json.dumps(title),
                                     content_type='application/json', headers=self.admin_header)
        self.assertEqual(response.status_code, 200)
        self.assertIn('book title modified', str(response.data))

        """Test if book is not available"""
        response_2 = self.client().put('/api/v2/admin/books/3', data=json.dumps(title),
                                       content_type='application/json', headers=self.admin_header)
        self.assertIn("book is not available", str(response_2.data))

    def test_modify_book_author(self):
        """Test API can modify book title"""
        author = {"author": "J.K Rowling"}
        response = self.client().put('/api/v2/admin/books/1', data=json.dumps(author),
                                     content_type='application/json', headers=self.admin_header)
        self.assertEqual(response.status_code, 200)
        self.assertIn('book author modified', str(response.data))

        """Test if book is not available"""
        response_2 = self.client().put('/api/v2/admin/books/3', data=json.dumps(author),
                                       content_type='application/json', headers=self.admin_header)
        self.assertIn("book is not available", str(response_2.data))

    def test_modify_book_copies(self):
        """Test API can modify book copies"""
        copies = {"copies": 50}
        response = self.client().put('/api/v2/admin/books/1', data=json.dumps(copies),
                                     content_type='application/json', headers=self.admin_header)
        self.assertEqual(response.status_code, 200)
        self.assertIn('book copies modified', str(response.data))

        """Test if book is not available"""
        response_2 = self.client().put('/api/v2/admin/books/3', data=json.dumps(copies),
                                       content_type='application/json', headers=self.admin_header)
        self.assertIn("book is not available", str(response_2.data))

    def test_modify_book_info(self):
        """Test API can return result if no book info is provided"""
        book_info = {}
        response = self.client().put('/api/v2/admin/books/1', data=json.dumps(book_info),
                                     content_type='application/json', headers=self.admin_header)
        self.assertEqual(response.status_code, 200)
        self.assertIn("At least one field is required", str(response.data))

    def test_delete_book(self):
        """Test API can delete book"""
        response = self.client().delete('/api/v2/admin/books/1', headers=self.admin_header)
        self.assertIn("book successfully deleted", str(response.data))
        self.assertEqual(response.status_code, 200)

    def test_get_all_users(self):
        """Test API can get all users"""
        response = self.client().get('/api/v2/admin/users', headers=self.admin_header)
        self.assertIn("admin", str(response.data))
        self.assertEqual(response.status_code, 200)

    def test_get_a_user(self):
        """Test API can get a user"""
        response = self.client().get('/api/v2/admin/users/1', headers=self.admin_header)
        self.assertEqual(response.status_code, 200)

        """Test API if it can get a user that is not available"""
        response_1 = self.client().get('/api/v2/admin/users/6', headers=self.admin_header)
        self.assertIn("user does not exist", str(response_1.data))
        self.assertEqual(response_1.status_code, 200)

    def test_reset_password(self):
        """Test API can reset password"""
        password = {"password": "987654321"}
        response = self.client().put('/api/v2/admin/users/1', data=json.dumps(password),
                                     content_type='application/json', headers=self.user_header)
        self.assertEqual(response.status_code, 200)
        self.assertIn("password changed!", str(response.data))

        """Test if user is not available"""
        response_2 = self.client().put('/api/v2/admin/users/8', data=json.dumps(password),
                                       content_type='application/json', headers=self.user_header)
        self.assertIn("user does not exist", str(response_2.data))

    def test_promote_user(self):
        """Test API can promote user"""
        response = self.client().patch('/api/v2/admin/users/1', headers=self.admin_header)
        self.assertEqual(response.status_code, 200)
        self.assertIn("user has been promoted", str(response.data))

        """Test if user is not available"""
        response_2 = self.client().patch('/api/v2/admin/users/8', headers=self.admin_header)
        self.assertIn("user does not exist", str(response_2.data))

    def test_delete_user(self):
        """Test API can delete a user"""
        response = self.client().delete('/api/v2/admin/users/1', headers=self.admin_header)
        self.assertEqual(response.status_code, 200)
        self.assertIn("user deleted", str(response.data))

        """Test API can delete a user that does not exists"""
        response = self.client().delete('/api/v2/admin/users/13', headers=self.admin_header)
        self.assertIn("user does not exist", str(response.data))

    def test_missing_admin_token(self):
        """Test API for missing token"""
        response = self.client().delete('/api/v2/admin/users/1')
        self.assertEqual(response.status_code, 401)
        self.assertIn("token missing", str(response.data))

    def test_invalid_token(self):
        """Test API for invalid token"""
        user_header = {"Content-Type": "application/json", "x-access-token": "qwertyuioasdfghj"}
        response = self.client().delete('/api/v2/admin/users/1', headers=user_header)
        self.assertEqual(response.status_code, 401)
        self.assertIn("kindly provide a valid token in the header", str(response.data))

    def test_not_admin_token(self):
        """Test API for not admin token"""
        response = self.client().delete('/api/v2/admin/users/1', headers=self.user_header)
        self.assertEqual(response.status_code, 401)
        self.assertIn("you are not authorized to perform this function as a non-admin user", str(response.data))



if __name__ == '__main__':
    unittest.main()
