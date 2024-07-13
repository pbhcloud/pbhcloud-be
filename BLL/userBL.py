def get_all_users(client):
    users = []
    users_cursor = client['pbhcloud-mongo-test']['users'].find({})
    for user in users_cursor:
        users.append(user)
    return users

def get_user_by_id(client, id):
    user = client['pbhcloud-mongo-test']['users'].find_one({"_id": id})
    return user

def get_users_count(client):
    db = client['pbhcloud-mongo-test']
    collection = db['users']
    doc_count = collection.count_documents({})
    return str(doc_count)