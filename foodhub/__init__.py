from flask import Flask
from dotenv import load_dotenv
import pymongo
import os
from flask_bcrypt import Bcrypt

load_dotenv()

uri= f"mongodb+srv://JaimitPatel:{os.getenv('MONGODB_PASS')}@cluster0.oc50jio.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = pymongo.MongoClient(uri)
db = client.AuthenticationData

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c2ef5ceadc6fac9ebf18423903ba4816'
bcrypt = Bcrypt(app)

from foodhub import routes