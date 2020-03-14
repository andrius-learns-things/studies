from celery import Celery
from events.event_store.mongo import MongoEventStore
from events.event_types import ADD_NEW_ITEM


app = Celery(broker="amqp://admin:password@rabbitmq:5672")
app.conf.beat_schedule = {
    "add_item": {"task": "add_item_periodically", "schedule": 30.0}
}


@app.task(bind=True, name="add_item_periodically")
def add_item_async(self):
    event_store = MongoEventStore()
    event_store.register_new_event(ADD_NEW_ITEM, {"name": "Periodically added item"})
