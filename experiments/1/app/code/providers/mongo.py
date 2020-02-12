from pymongo import MongoClient


client = MongoClient("mongo", 27017)
mongodb = client.hits_db


def get_hit_count():
    mongodb.hits_db.insert_one({'hit': 'yes?'})
    return len([item for item in mongodb.hits_db.find()])
