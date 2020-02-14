from pymongo import MongoClient
from .base import Provider


class MongoProvider(Provider):
    def __init__(self):
        client = MongoClient("mongo", 27017)
        self.mongodb = client.hits_db

    @property
    def name(self):
        return "Mongo"

    def get_hit_count(self):
        self.mongodb.hits_db.insert_one({"hit": "yes?"})
        return len([item for item in self.mongodb.hits_db.find()])
