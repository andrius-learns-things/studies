from pymongo import MongoClient
from .base import Provider


class MongoProvider(Provider):
    def __init__(self):
        client = MongoClient("mongo", 27017)
        self.mongodb = client.main_db

    @property
    def name(self):
        return "Mongo"

    def get_hit_count(self):
        self.mongodb.hits.insert_one({"hit": "yes?"})
        return len([item for item in self.mongodb.hits.find()])

    def clear_persons(self):
        self.mongodb.persons.drop()

    def register_person(self, person):
        self.mongodb.persons.insert_one(person)

    def search_persons(self, field, value):
        return [p for p in self.mongodb.persons.find({field: value})]
