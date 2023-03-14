from helloapp import app
import unittest
from urllib import request

class TestHelloAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertIn(b'{"message": "Hello World!!!"}', response.data)
        
    def test_hello_world2(self):
        response = self.app.get('/index/')
        self.assertIn(b'{"message": "Hello World!!!"}', response.data)