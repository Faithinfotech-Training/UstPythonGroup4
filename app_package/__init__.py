from flask import Flask
from app_package.config import Config
from flask_pymongo import PyMongo

app=Flask(__name__)
app.config.from_object(Config)
mongo=PyMongo(app)


from app_package import batch_routes,course_routes