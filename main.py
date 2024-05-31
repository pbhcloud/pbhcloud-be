from fastapi import FastAPI
from BLL import userBL

app = FastAPI()

# Create an S3 client for IDrive e2
# endpoint = "l4g4.ch11.idrivee2-2.com"
# client = boto3.client("s3", endpoint_url='process.env.endpoint')

# # Get list of objects in bucket 'my-bucket'
# print(client.list_objects(Bucket="my-bucket"))



@app.get("/")
async def root():
    return {"message": "Hello World"}

# Shouldn't be accessible for normal users
@app.get('/system/all-users')
def get_all_users(self):
    users = userBL.get_all_users(self)
    return users