from pymongo import MongoClient

from Zibal.settings import MONGO_DB_NAME, MONGO_DB_URI

client = MongoClient(MONGO_DB_URI)

db = client[MONGO_DB_NAME]

try:
    print("Connected to MongoDB!")

    collections = db.list_collection_names()
    print("Collections in database:", collections)
except Exception as e:
    print("Failed to connect to MongoDB:", e)

