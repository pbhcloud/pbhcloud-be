from flask import Flask, jsonify, url_for, request
from flask_cors import CORS
# from datetime import datetime
import os
# from pymongo.collection import Collection, ReturnDocument
from pymongo import MongoClient
# from pymongo.errors import DuplicateKeyError

from BLL import userBL
# from .models.userModel import User
# from .objectid import PydanticObjectId


app = Flask(__name__)
cors = CORS(app, origins='*')
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
# pymongo = MongoClient(app)

@app.route('/')
def home():
    return 'hello world'

@app.route('/api/getusers', methods=['GET'])
def users():
    return {
            'users': [
                'arpan', 'michael', 'jess'
            ]
        }


# Shouldn't be accessible for normal users
@app.get('/system/all-users')
def get_all_users(self):
    users = userBL.get_all_users(self)
    return users

if __name__ == '__main__':
    app.run(debug=True, port=5000)