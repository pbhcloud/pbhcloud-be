from flask import Flask, jsonify, url_for, request
from flask_cors import CORS
import os
# from pymongo.collection import Collection, ReturnDocument
# from pymongo.errors import DuplicateKeyError

from BLL import userBL
# from .models.userModel import User
# from .objectid import PydanticObjectId
from configs import mongo 

app = Flask(__name__)
cors = CORS(app, origins='*')
client = mongo.mongoConfig()

@app.route('/')
def home():
    return 'hello world'

@app.route('/api/getusers', methods=['GET'])
def users():
    return str(userBL.get_all_users(client))


# Shouldn't be accessible for normal users
@app.get('/system/all-users')
def get_all_users():
    # users = userBL.get_all_users(self)
    return mongo.mongoConfig()

if __name__ == '__main__':
    app.run(debug=True, port=5000)