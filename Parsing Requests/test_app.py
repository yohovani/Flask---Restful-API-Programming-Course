from blogs_app import app
import unittest
from urllib import request
import datetime

class TestBlogsAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_blogs_api_case1(self):
        blog = {'title' : 'Python Application Programming',
                'article_text': 'This article talks about Python and illustrates how Python is used in application programming, with examples.',
                }
        response = self.client.post('/blogs/1/', data=blog)
        self.assertIn(b'"title": "Python Application Programming"', response.data)
        self.assertIn(b'"article_text": "This article talks about Python and illustrates how Python is used in application programming, with examples."', response.data)
        
        
    def test_blogs_api_case2(self):
        blog = {'title' : 'Flask - A Micro Web Framework in Python',
                'article_text': 'This article talks about Flask framework. It can be used to build web apps in a quick time.',
                }
        response = self.client.post('/blogs/2/', data=blog)
        self.assertIn(b'"title": "Flask - A Micro Web Framework in Python"', response.data)
        self.assertIn(b'"article_text": "This article talks about Flask framework. It can be used to build web apps in a quick time."', response.data)
        
    def test_blogs_api_case3(self):
        blog = {'title' : 'Flask-RESTful - Flask Extension for building REST APIs',
                'article_text': 'This article introduces you to Flask-RESTful, an extension used for building REST APIs in Flask.',
                }
        response = self.client.post('/blogs/3/', data=blog)
        self.assertIn(b'"title": "Flask-RESTful - Flask Extension for building REST APIs"', response.data)
        self.assertIn(b'"article_text": "This article introduces you to Flask-RESTful, an extension used for building REST APIs in Flask."', response.data)
        
    def test_blogs_api_case4(self):
        response = self.client.get('/blogs/')
        self.assertIn(b'"title": "Python Application Programming"', response.data)
        self.assertIn(b'"article_text": "This article talks about Python and illustrates how Python is used in application programming, with examples."', response.data)
        self.assertIn(b'"title": "Flask - A Micro Web Framework in Python"', response.data)
        self.assertIn(b'"article_text": "This article talks about Flask framework. It can be used to build web apps in a quick time."', response.data)
        self.assertIn(b'"title": "Flask-RESTful - Flask Extension for building REST APIs"', response.data)
        self.assertIn(b'"article_text": "This article introduces you to Flask-RESTful, an extension used for building REST APIs in Flask."', response.data)
        
    def test_blogs_api_case5(self):
        response = self.client.get('/blogs/3/')
        self.assertNotIn(b'"title": "Python Application Programming"', response.data)
        self.assertNotIn(b'"article_text": "This article talks about Python and illustrates how Python is used in application programming, with examples."', response.data)
        self.assertNotIn(b'"title": "Flask - A Micro Web Framework in Python"', response.data)
        self.assertNotIn(b'"article_text": "This article talks about Flask framework. It can be used to build web apps in a quick time."', response.data)
        self.assertIn(b'"title": "Flask-RESTful - Flask Extension for building REST APIs"', response.data)
        self.assertIn(b'"article_text": "This article introduces you to Flask-RESTful, an extension used for building REST APIs in Flask."', response.data)
    
        
    def test_blogs_api_case6(self):
        response = self.client.delete('/blogs/3/')
        self.assertIn(b'Blog with Id 3 is deleted', response.data)
        response = self.client.get('/blogs/')
        self.assertIn(b'"title": "Python Application Programming"', response.data)
        self.assertIn(b'"article_text": "This article talks about Python and illustrates how Python is used in application programming, with examples."', response.data)
        self.assertIn(b'"title": "Flask - A Micro Web Framework in Python"', response.data)
        self.assertIn(b'"article_text": "This article talks about Flask framework. It can be used to build web apps in a quick time."', response.data)
        self.assertNotIn(b'"title": "Flask-RESTful - Flask Extension for building REST APIs"', response.data)
        self.assertNotIn(b'"article_text": "This article introduces you to Flask-RESTful, an extension used for building REST APIs in Flask."', response.data)
        
    def test_blogs_api_case7(self):
        response = self.client.delete('/blogs/6/')
        self.assertIn(b"Blog_Id 6 doesn't exist", response.data)
        
    def test_blogs_api_case8(self):
        blog = {'title' : 'PYTHON APPLICATION PROGRAMMING',
                'article_text' : 'This article talks about Python and illustrates how Python is used in application programming, with examples.'
                }
        response = self.client.put('/blogs/7/', data=blog)

        self.assertIn(b"Blog_Id 7 doesn't exist", response.data)
        
    def test_blogs_api_case9(self):
        blog = {'title' : 'PYTHON APPLICATION PROGRAMMING',
            'article_text' : 'This article talks about Python and illustrates how Python is used in application programming, with examples.'
        }
        response = self.client.put('/blogs/1/', data=blog)
        
        self.assertIn(b'"title": "PYTHON APPLICATION PROGRAMMING"', response.data)
        self.assertIn(b'"article_text": "This article talks about Python and illustrates how Python is used in application programming, with examples."', response.data)
    
        
    
