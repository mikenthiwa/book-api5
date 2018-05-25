import unittest
import sys  # fix import errors
import os
import json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import db, create_app


class ConfigTestCase(unittest.TestCase):
    """This class represents the books test case"""

    def setUp(self):
        """Define test variables and initialize app"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.book = {"title": "The Storm", "author": "Blake Banner", "copies": 8}
        self.title = self.book["title"]
        self.author = self.book["author"]
        self.copies = self.book["copies"]
        # binds the app to the current context
        with self.app.app_context():
            # create all tables

            db.create_all()

            self.client().post('/api/v2/admin/books',
                               data=json.dumps(self.book),
                               content_type='application/json')

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()
