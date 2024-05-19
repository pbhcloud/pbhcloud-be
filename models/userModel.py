import pymongo
from pymongo import MongoClient
import bcrypt
import validator

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["your_database_name"]

# Define the user schema
user_schema = {
    "name": {"type": str, "required": True},
    "email": {
        "type": str,
        "required": True,
        "unique": True,
        "lowercase": True,
        "validate": validator.is_email,
    },
    "picture": {"type": str, "default": "https://res.cloudinary.com/dkd5jblv5/image/upload/v1675976806/Default_ProfilePicture_gjngnb.png"},
    "password": {
        "type": str,
        "required": True,
        "min_length": 6,
        "max_length": 48,
    },
}

# Create the user collection
users = db["users"]

# Define a pre-save hook to hash the password
def hash_password(next):
    def wrapper():
        if self.is_new:
            salt = bcrypt.gensalt(12)
            hashed_password = bcrypt.hashpw(self.password.encode(), salt)
            self.password = hashed_password.decode()
        next()

    return wrapper

# Add the pre-save hook to the user schema
user_schema["pre_save"] = hash_password

# Create the UserModel class
class UserModel:
    def __init__(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)

    def save(self):
        users.insert_one(self.__dict__)

# Instantiate the UserModel
UserModel = UserModel(**user_schema)

# Example usage:
new_user = UserModel(name="John Doe", email="john@example.com", password="my_secure_password")
new_user.save()
