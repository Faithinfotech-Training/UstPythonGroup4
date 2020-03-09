import os

class Config(object):
    SECRET_KEY=os.urandom(24).hex()

    SQLALCHEMY_DATABASE_URI="mysql+pymysql://flaskuser:flaskuser@localhost/studdb"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    MONGO_URI="mongodb://localhost:27017/tamsdata"
    

  

