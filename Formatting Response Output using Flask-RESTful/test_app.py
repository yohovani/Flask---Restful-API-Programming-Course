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
        self.assertTrue('title' in response.json)
        self.assertTrue('article_text' in response.json)
        self.assertTrue('created_at' in response.json)
        self.assertEqual('Python Application Programming', response.json['title'])
        self.assertEqual('This article talks about Python and illustrates how Python is used in application programming, with examples.', response.json['article_text'])
        
        
    def test_blogs_api_case2(self):
        blog = {'title' : 'Flask - A Micro Web Framework in Python',
                'article_text': 'This article talks about Flask framework. It can be used to build web apps in a quick time.',
                }
        response = self.client.post('/blogs/2/', data=blog)
        self.assertTrue('title' in response.json)
        self.assertTrue('article_text' in response.json)
        self.assertTrue('created_at' in response.json)
        self.assertTrue('Flask - A Micro Web Framework in Python', response.json['title'])
        self.assertTrue('This article talks about Flask framework. It can be used to build web apps in a quick time.', response.json['article_text'])

        
    def test_blogs_api_case3(self):
        blog = {'title' : 'Flask-RESTful - Flask Extension for building REST APIs',
                'article_text': 'This article introduces you to Flask-RESTful, an extension used for building REST APIs in Flask.',
                }
        response = self.client.post('/blogs/3/', data=blog)
        self.assertTrue('title' in response.json)
        self.assertTrue('article_text' in response.json)
        self.assertTrue('created_at' in response.json)
        self.assertTrue('Flask-RESTful - Flask Extension for building REST APIs', response.json['title'])
        self.assertTrue('This article introduces you to Flask-RESTful, an extension used for building REST APIs in Flask.', response.json['article_text'])
        
    def test_blogs_api_case4(self):
        response = self.client.get('/blogs/')
        #print(response.json)
        #self.assertTrue(1 in response.json)
        #self.assertTrue(2 in response.json)
        #self.assertTrue(3 in response.json)
        self.assertTrue('title' in response.json[0])
        self.assertTrue('article_text' in response.json[0])
        self.assertTrue('created_at' in response.json[0])
        self.assertEqual('Python Application Programming', response.json[0]['title'])
        self.assertEqual('This article talks about Python and illustrates how Python is used in application programming, with examples.', response.json[0]['article_text'])

        self.assertTrue('title' in response.json[1])
        self.assertTrue('article_text' in response.json[1])
        self.assertTrue('created_at' in response.json[1])
        self.assertTrue('Flask - A Micro Web Framework in Python', response.json[1]['title'])
        self.assertTrue('This article talks about Flask framework. It can be used to build web apps in a quick time.', response.json[1]['article_text'])
        self.assertTrue('title' in response.json[2])
        self.assertTrue('article_text' in response.json[2])
        self.assertTrue('created_at' in response.json[2])
        self.assertTrue('Flask-RESTful - Flask Extension for building REST APIs', response.json[2]['title'])
        self.assertTrue('This article introduces you to Flask-RESTful, an extension used for building REST APIs in Flask.', response.json[2]['article_text'])
        
        
    def test_blogs_api_case5(self):
        response = self.client.get('/blogs/3/')
        print(response.json)
    
        self.assertTrue('title' in response.json)
        self.assertTrue('article_text' in response.json)
        self.assertTrue('created_at' in response.json)
        self.assertTrue('Flask-RESTful - Flask Extension for building REST APIs', response.json['title'])
        self.assertTrue('This article introduces you to Flask-RESTful, an extension used for building REST APIs in Flask.', response.json['article_text'])
        
        
    def test_blogs_api_case6(self):
        response = self.client.delete('/blogs/3/')
        self.assertIn(b'Blog with Id 3 is deleted', response.data)
        response = self.client.get('/blogs/')
        #self.assertTrue(1 in response.json)
        #self.assertTrue(2 in response.json)
        #self.assertFalse(3 in response.json)
        self.assertTrue('title' in response.json[0])
        self.assertTrue('article_text' in response.json[0])
        self.assertTrue('created_at' in response.json[0])
        self.assertEqual('Python Application Programming', response.json[0]['title'])
        self.assertEqual('This article talks about Python and illustrates how Python is used in application programming, with examples.', response.json[0]['article_text'])

        self.assertTrue('title' in response.json[1])
        self.assertTrue('article_text' in response.json[1])
        self.assertTrue('created_at' in response.json[1])
        self.assertTrue('Flask - A Micro Web Framework in Python', response.json[1]['title'])
        self.assertTrue('This article talks about Flask framework. It can be used to build web apps in a quick time.', response.json[1]['article_text'])
        
        
    def test_blogs_api_case7(self):
        response = self.client.delete('/blogs/6/')
        print(response.json)
        self.assertIn(b"Blog_Id 6 doesn't exist", response.data)
        
    def test_blogs_api_case8(self):
        blog = {'title' : 'PYTHON APPLICATION PROGRAMMING',
                'article_text' :"This article talks about Python and illustrates how Python is used in application programming, with examples."
                }
        response = self.client.put('/blogs/7/', data=blog)

        self.assertIn(b"Blog_Id 7 doesn't exist", response.data)
        
    def test_blogs_api_case9(self):
        blog = {'title' : 'PYTHON APPLICATION PROGRAMMING',
               'article_text' :"This article talks about Python and illustrates how Python is used in application programming, with examples."
               }
        response = self.client.put('/blogs/1/', data=blog)

        self.assertTrue('title' in response.json)
        self.assertTrue('article_text' in response.json)
        self.assertTrue('created_at' in response.json)
        self.assertEqual('PYTHON APPLICATION PROGRAMMING', response.json['title'])
        self.assertEqual('This article talks about Python and illustrates how Python is used in application programming, with examples.', response.json['article_text'])
        
    
    
        
    
