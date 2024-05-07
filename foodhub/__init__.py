from flask import Flask
from dotenv import load_dotenv
import pymongo
import os
from flask_bcrypt import Bcrypt

load_dotenv()

# uri= f"mongodb+srv://JaimitPatel:{os.getenv('MONGODB_PASS')}@cluster0.oc50jio.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
uri = "mongodb://localhost:27017/"
client = pymongo.MongoClient(uri)
db = client[os.getenv('DB_NAME')][os.getenv('COLLECTION_NAME')]

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
bcrypt = Bcrypt(app)

from foodhub import routes