from celery import Celery


app = Celery(broker="amqp://admin:password@rabbitmq:5672", include=["tasks"])


app.conf.beat_schedule = {"refresh": {"task": "add_item_async", "schedule": 30.0}}


@app.task(bind=True, name="add_item_async")
def add_item_async(self, urls):
    print("Doing smth")
