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
        self.mongodb.orgs.drop()
        self.mongodb.registrations.drop()
        self.mongodb.registrations.create_index([("subsystem", DESCENDING)])

    def register_org(self, org, registration):

        org = self.mongodb.orgs.find_one({"name": org["name"]})

        if not org:
            org_id = self.mongodb.orgs.insert_one(org)
        else:
            org_id = org["id"]

        registration["org_id"] = org_id

        self.mongodb.registrations.insert_one(registration)

    def get_last_registered_orgs(self, subsystem):
        return [r for r in self.mongodb.registrations.find({"subsystem": subsystem})]
