import pika


class RabbitMQProvider:
    def post(self, msg):
        credentials = pika.PlainCredentials("admin", "password")
        parameters = pika.ConnectionParameters("rabbitmq", 5672, "/", credentials)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue="items")
        channel.basic_publish(exchange="", routing_key="items", body=msg)
        connection.close()
