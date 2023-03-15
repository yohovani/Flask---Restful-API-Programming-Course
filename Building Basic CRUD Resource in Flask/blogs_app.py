from flask import Flask, request
from flask_restful import Resource, Api, abort
from datetime import datetime
app = Flask(__name__)
api = Api(app)
                 
                 
blogs = {1:{'title':"test",'article_text':"request.form.get('article_text')",'created_at':datetime.today().strftime('%Y-%m-%d %H:%M:%S')}}

class BlogsAPI(Resource):
    def get(self, blog_id=None):
        '''Return 'blogs' dictionary if 'blog_id' is None.
        
           if blog_id is provided,
           Abort the request if 'blog_id' and not in keys of 'blogs' dictionary, or else
           Return the blog corresponding to given 'blog_id'
        '''
        print(blog_id)
        if blog_id == None:
          return blogs
        else:
          if blog_id in blogs:
            return blogs[blog_id]
        abort(404, description="Blog not Found.")

    def post(self, blog_id):
        '''
        If 'blog_id' is not in keys of 'blogs' dictionary, create a new dictionary object
        'blog', with three keys 'title', 'article_text', and 'created_at'.
        The values of 'title', and 'article_text' to be captured from http form varaibles :
        'title', 'article_text.
        The value of 'created_at' must be current date time string represented by format '%Y-%m-%d %H:%M:%S'
        
        Add the created dictionary object to 'blogs' dictionary with key corresponding to given 'blog_id',
        and Return the created dictionary object.
        
        If 'blog_id' is in keys of 'blogs' dictionary, abort the request.
        '''
        if blog_id not in blogs.keys():
          blog = {'title':request.form.get("title"),'article_text':request.form.get("article_text"),'created_at':datetime.today().strftime('%Y-%m-%d %H:%M:%S')}
          blogs[blog_id] = blog
          return blog
        abort(404, description="Blog not Found.")

    def put(self, blog_id):
        '''
        If given 'blog_id' not in 'blogs' dictionary abort the request with 404 status code and message like shown below.
        
        Sample Error message : "Blog_Id 2 doesn't exist"
        
        Else, update the details of blog, identified by given 'blog_id', and return the updated blog details.
        '''
        if blog_id not in blogs:
          abort(404,message="Blog_Id "+str(blog_id)+" doesn't exist")
        else:
            dic_aux = {}
            if request.form.get("title"):
              blogs[blog_id]["title"] = request.form.get("title")
            if request.form.get("article_text"):
              blogs[blog_id]["article_text"] = request.form.get("article_text")
            
            return blogs[blog_id]

    def delete(self, blog_id):
        '''
        If 'blog_id' not in keys of 'blogs' dictionary, abort the request with 404 status code and message like shown below.
        
        Sample Error message : "Blog_Id 2 doesn't exist"
        
        Else delete the blog corresponding to given 'blog_id' from 'blogs' dictionary and respond with a message like shown below.
        
        Sample Delete response message : "Blog with Id 3 is deleted"
        '''
        if blog_id not in blogs:
          abort(404,message="Blog_Id "+str(blog_id)+" doesn't exist")
        else:
            blogs.pop(blog_id)
            return {"message":"Blog with Id "+str(blog_id)+" is deleted"}

        
    
api.add_resource(BlogsAPI, '/blogs/',
                              '/blogs/<int:blog_id>/')

if __name__ == '__main__':
    app.run()