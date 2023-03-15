from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse, fields, marshal_with, marshal
import datetime as dt

app = Flask(__name__)
api = Api(app)
               
blogsParser = reqparse.RequestParser()
blogsParser.add_argument('title', required=True, type=str)
blogsParser.add_argument('article_text', required=True, type=str)

# Create a dictionary named 'blog_fields' with
# three fields 'title', 'article_text' and
# 'created_at' as string type.


blogs = {}
blog_fields = {'title':fields.String,
'article_text':fields.String,
'created_at':fields.String}
class BlogsAPI(Resource):
    @marshal_with(blog_fields)
    def get(self, blog_id=None):
        '''Return 'blogs' dictionary if 'blog_id' is None.
        
           if blog_id is provided,
           Abort the request if 'blog_id' and not in keys of 'blogs' dictionary, or else
           Return the blog corresponding to given 'blog_id'
           
        '''
        if blog_id is None:
            return [ blogs[blog_id] for blog_id in blogs ]
        if blog_id not in blogs:
            abort(404, message="Blog_Id {} doesn't exist".format(blog_id))
        return blogs[blog_id]
    
    @marshal_with(blog_fields)
    def post(self, blog_id):
        '''
        Access the input arguments in a dictionary named 'args'
        
        If 'blog_id' is not in keys of 'blogs' dictionary, create a new dictionary object
        'blog', with three keys 'title', 'article_text', and 'created_at'
        The values of them have to be captured from http form varaibles :
        'title', 'article', and 'created_at'. 
        
        Add the created dictionary object to 'blogs' dictionary with key corresponding to given 'blog_id',
        and Return the created dictionary object.
        
        'created_at' should be datetime.datetime object
        
        If 'blog_id' is in keys of 'blogs' dictionary, abort the request.
        '''
        
        blog_args = blogsParser.parse_args()
        if blog_id not in blogs:
            blog = {}
            
            blog['title'] = blog_args['title']
            blog['article_text'] = blog_args['article_text']
            created_at = dt.datetime.now()
            blog['created_at'] = created_at.strftime('%Y-%m-%d %H:%M:%S')
            blogs[blog_id] = blog
            return blogs[blog_id]
        abort(404, message="Blog_Id {} already exists".format(blog_id))
    
    @marshal_with(blog_fields)
    def put(self, blog_id):
        '''
        Access the input arguments in a dictionary named 'args'
        
        If given 'blog_id' not in 'blogs' dictionary abort the request.
        
        Else, update the details of blog, identified by given 'blog_id', and return the updated blog details.
        '''
        blog_args = blogsParser.parse_args()
        if blog_id in blogs:
            blog = {}
            
            blog['title'] = blog_args['title']
            blog['article_text'] = blog_args['article_text']
            
            blogs[blog_id].update(blog)
            return blogs[blog_id]
        abort(404, message="Blog_Id {} doesn't exist".format(blog_id))
    
    def delete(self, blog_id):
        '''
        If 'blog_id' not in keys of 'blogs' dictionary, abort the request. 
        
        Else delete the blog corresponding to given 'blog_id' from 'blogs' dictionary.
        '''
        if blog_id in blogs:
            response_string = 'Blog with Id {} is deleted'.format(blog_id)
            del blogs[blog_id]
            return response_string
        abort(404, message="Blog_Id {} doesn't exist".format(blog_id))
    
api.add_resource(BlogsAPI, '/blogs/',
                              '/blogs/<int:blog_id>/')

if __name__ == '__main__':
    app.run()