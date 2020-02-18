from pymongo import MongoClient, DESCENDING
from .base import Provider


class MongoProvider(Provider):

    # Constructor

    def __init__(self):
        client = MongoClient("mongo", 27017)
        self.mongodb = client.main_db

    # Provider meta props

    @property
    def name(self):
        return "Mongo"

    # Hit count experiment

    def get_hit_count(self):
        self.mongodb.hits.insert_one({"hit": "yes?"})
        return len([item for item in self.mongodb.hits.find()])

    # Single entity experiment

    def ensure_empty_person_structure(self):
        self.mongodb.persons.drop()

    def register_person(self, person):
        self.mongodb.persons.insert_one(person)

    def search_persons(self, field, value):
        return [p for p in self.mongodb.persons.find({field: value})]

    def add_person_indexes(self):
        self.mongodb.persons.create_index([("first_name", DESCENDING)])

    # Two entities experiment

    def ensure_empty_org_structures(self):
        pass

    def register_org(self, org, registration):
        pass

    def get_last_registered_orgs(self, subsystem):
        return []
