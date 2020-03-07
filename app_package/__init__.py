from flask import Flask
from app_package.config import Config
from flask_pymongo import PyMongo

app=Flask(__name__)
app.config.from_object(Config)
mongo=PyMongo(app)
<<<<<<< HEAD
#login_manager=LoginManager(app)
#login_manager.login_view="index"

from app_package import enquiry_routes,admission_routes
=======


from app_package import batch_routes,course_routes,resource_routes
>>>>>>> 21d52a27123166d28fb27a267aa64170c1f20309
