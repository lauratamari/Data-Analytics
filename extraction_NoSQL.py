from pymongo import MongoClient
client = MongoClient('mongodb://user:password@localhost/database_name')
db = client['database_name']

collection = db['collection_name']
data = collection.find({})