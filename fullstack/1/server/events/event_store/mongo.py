from pymongo import MongoClient, ASCENDING
from .base import BaseEventStore


class MongoEventStore(BaseEventStore):

    # Constructor

    def __init__(self):
        client = MongoClient("mongo", 27017)
        self.mongodb = client.main_db
        self.mongodb.events.create_index([("index", ASCENDING)])

    # Event store methods

    def register_new_event(self, type, payload=None):
        event_index = self.mongodb.events.count() + 1
        event = {"index": event_index, "type": type, "payload": payload}
        self.mongodb.events.insert_one(event)

    def get_events(self, start_index, end_index=None):
        index_query = {"$gte": start_index}
        if end_index:
            index_query["$lte"] = end_index
        return list(
            self.mongodb.events.find({"index": index_query}).sort(
                [("index", ASCENDING)]
            )
        )
