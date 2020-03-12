import pika


class RabbitMQProvider:
    def post(self, msg):
        connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
        channel = connection.channel()
        channel.queue_declare(queue="items")
        channel.basic_publish(exchange="", routing_key="items", body=msg)
        connection.close()
