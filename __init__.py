import pymongo
import os
from flask_pymongo import PyMongo

MONGO_URL = os.environ.get('MONGO_URL')
if not MONGO_URL:
    MONGO_URL = "mongodb://localhost:27017/mars_mission_app";


app.config['MONGO_URI'] = MONGO_URL
mongo = PyMongo(app)

#client = pymongo.MongoClient(conn)


# if database mars_mission_app exists, nothing will be done

dblist = mongo.list_database_names()
if "mars_mission_app" in dblist:
    print("The database exists.")
else:
    db = mongo.mars_mission_app

