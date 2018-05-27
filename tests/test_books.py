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
        response = self.client().get('/api/v2/auth/users/books/1', headers=self.user_header)
        self.assertEqual(response.status_code, 200)
        self.assertIn("The Storm", str(response.data))

