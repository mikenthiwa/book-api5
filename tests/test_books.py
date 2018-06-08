#  test_borrowed book
import unittest
import json
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.config_tests import ConfigTestCase


class BorrowedBookEndPoint(ConfigTestCase):
    """This class represents borrowed book test cases """

    def test_borrowed_book(self):
        """Test API can access protected route using a token"""
        response = self.client().get('/api/v2/auth/users/books/1', headers=self.user_header)
        self.assertEqual(response.status_code, 200)
        self.assertIn("The Storm", str(response.data))

    def test_invalid_token_provided(self):
        """Test API when invalid token is provided"""
        user_header = {"Content-Type": "application/json", "x-access-token": "qwertyuioasdfghj"}
        response = self.client().get('/api/v2/auth/users/books/1', headers=user_header)
        self.assertIn("kindly provide a valid token in the header", str(response.data))

    def test_missing_token(self):
        """Test API when token is missing"""
        user_header = {"Content-Type": "application/json"}
        response = self.client().get('/api/v2/auth/users/books/1', headers=user_header)
        self.assertIn("token missing", str(response.data))


