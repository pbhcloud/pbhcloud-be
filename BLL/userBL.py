def get_all_users(self):
    users = []
    users_cursor = self.client['testDB']['users'].find({})
    for user in users_cursor:
        users.append(user)
    return users

def get_user_by_id(self, id):
    user = self.client['testDB']['users'].find_one({"_id": ObjectId(id)})
    return user