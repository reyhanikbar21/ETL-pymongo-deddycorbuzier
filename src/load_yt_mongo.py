import pymongo
from pymongo import MongoClient


def jsonlist_to_mongodb(jsonlist,url,database,collection):
    cluster = MongoClient(url)
    db = cluster[database]
    collection = db[collection]
    for document in jsonlist:
        collection.update_many(
            {'_id': document['_id']},
            {'$setOnInsert': document},
            upsert=True 
        )
    