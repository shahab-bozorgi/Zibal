from datetime import datetime

from bson import ObjectId
from pymongo import MongoClient

from Zibal.settings import MONGO_DB_NAME, MONGO_DB_URI
from transactions.models import Transaction

client = MongoClient(MONGO_DB_URI)

db = client[MONGO_DB_NAME]

try:
    print("Connected to MongoDB!")

    collections = db.list_collection_names()
    print("Collections in database:", collections)
except Exception as e:
    print("Failed to connect to MongoDB:", e)

print(Transaction._fields)  # این باید تمام فیلدهای مدل را نشان دهد

# transaction = Transaction(
#     merchantId=ObjectId('63a69a2d18f9347bd89d5f88'),  # استفاده از ObjectId به این شکل
#     amount=100000,
#     createdAt=datetime.now()
# )
# transaction.save()