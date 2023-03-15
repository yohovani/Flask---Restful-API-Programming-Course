from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse
from datetime import datetime

app = Flask(__name__)
api = Api(app)

# Define a variable 'blogsParser', an instance of 'reqparse.RequestParser' and
# add the arguments 'title', and 'article_text'
# 'title' must be a string and a required argument.
# 'article_text' must be a string and a required argument.
blogsParser = reqparse.RequestParser()
blogsParser.add_argument('title', required=True, type=str, help="store the title of the blog")
blogsParser.add_argument('article_text', required=True, type=str, help="store the content of the article")
blogs = {}

class BlogsAPI(Resource):
  def get(self, blog_id=None):
    if blog_id == None:
      return blogs
    else:
      if blog_id in blogs:
        return blogs[blog_id]
    abort(404, description="Blog not Found.")

  def post(self, blog_id):
    args = blogsParser.parse_args()
    if blog_id not in blogs.keys():
      blog = {'title':args["title"],'article_text':args["article_text"],'created_at':datetime.today().strftime('%Y-%m-%d %H:%M:%S')}
      blogs[blog_id] = blog
      return blog
    abort(404, description="Blog not Found.")

  def put(self, blog_id):
    args = blogsParser.parse_args()
    if blog_id not in blogs:
      abort(404,message="Blog_Id "+str(blog_id)+" doesn't exist")
    else:
      if request.form.get("title"):
        blogs[blog_id]["title"] = args["title"]
      if request.form.get("article_text"):
        blogs[blog_id]["article_text"] = args["article_text"]
            
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