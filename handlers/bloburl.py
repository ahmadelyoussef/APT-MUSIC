import json
import webapp2
from google.appengine.api import users
from google.appengine.ext import blobstore

            
class MediaUploadFormHandler(webapp2.RequestHandler):
    def post(self):
        user=users.get_current_user()
        if user:
            upload_url = blobstore.create_upload_url('/_ah/upload')
            self.response.headers["Content-Type"] = "application/json"

            res = {
                'code': 200,
                'response':upload_url
                 }
            #print upload_url
            print json.dumps(res)
            self.response.write(json.dumps(res))




            