from flask import Flask
from app_package.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_pymongo import PyMongo
from flask_login import LoginManager

app=Flask(__name__)
app.config.from_object(Config)
mongo=PyMongo(app)
db=SQLAlchemy(app)
migrate=Migrate(app,db)
login_manager=LoginManager(app)
login_manager.login_view="index"


from app_package import batch_routes,course_routes,resource_routes,enquiry_routes,admission_routes,module_routes,qualification_routes

