import os
from app import app
import unittest

class HomeTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_home(self):
        rv = self.app.get('/')
        assert '' in rv.data

if __name__ == '__main__':
    unittest.main()
