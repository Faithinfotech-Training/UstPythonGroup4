import os

class Config(object):
    SECRET_KEY=os.urandom(24).hex()
    MONGO_URI="mongodb://localhost:27017/tamsdb"