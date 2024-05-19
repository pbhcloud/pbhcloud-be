
from pymongo import MongoClient
# https://github.com/mongodb-university/atlas_starter_python/blob/master/atlas-starter.py should be reviewed.
uri = ""

client = MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile='<path_to_certificate>',
                     server_api=ServerApi('1'))

db = client['testDB']
collection = db['users']
doc_count = collection.count_documents({})
print(doc_count)
