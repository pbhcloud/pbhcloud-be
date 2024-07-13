from pydantic import BaseModel, Field
from typing import List, Optional, Union
from pymongo import MongoClient
from datetime import datetime
from ..objectid import PydanticObjectId
import json
class User(BaseModel):
    id: Optional[PydanticObjectId] = Field(None, alias="_id")
    name: str
    email: str
    picture: str
    password: str
    rootFolder: str
    settings: list
    creationDate: int= int(datetime.timestamp(datetime.now()))

    def to_json(self):
        return json.dumps(self, execlude_none=True)
    
    def to_bson(self):
        data = self.dict(by_alias=True, exclude_none=True)
        if data.get("_id") is None:
            data.pop("_id", None)
        return data

# Define the user schema
# user_schema = {
#     "name": {"type": str, "required": True},
#     "email": {
#         "type": str,
#         "required": True,
#         "unique": True,
#         "lowercase": True,
#         "validate": validator.is_email,
#     },
#     "picture": {"type": str, "default": "https://res.cloudinary.com/dkd5jblv5/image/upload/v1675976806/Default_ProfilePicture_gjngnb.png"},
#     "password": {
#         "type": str,
#         "required": True,
#         "min_length": 6,
#         "max_length": 48,
#     },
#     "rootFolder": {"type": object, }, #TODO - Gotta verify later on what should be added here to define rootFolder a bit better.
#     "settings": {"type": list, "default": [], "required": True}, #Currently, in document its written as obj although I think we can handle settings as a JSON list or something like that.
# }

# #TODO- Define a pre-save hook to hash the password

# #TODO- Add the pre-save hook to the user schema
# # user_schema["pre_save"] = hash_password

# # Create the UserModel class
# class UserModel:
#     def __init__(self, **kwargs):
#         for field, value in kwargs.items():
#             setattr(self, field, value)

#     def save(self):
#         users.insert_one(self.__dict__)

# # Instantiate the UserModel
# UserModel = UserModel(**user_schema)

# # Example usage:
# new_user = UserModel(name="John Doe", email="john@example.com", password="my_secure_password")
# new_user.save()
