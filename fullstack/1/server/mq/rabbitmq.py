import pika


class RabbitMQProvider:
    def post(self, msg):
        connection, channel = self._get_connection_and_channel()
        channel.basic_publish(exchange="", routing_key="items", body=msg)
        connection.close()

    def get_all(self):
        connection, channel = self._get_connection_and_channel(passive=True)

        messages = []
        ok = True

        while ok:
            method_frame, header_frame, body = channel.basic_get("items", auto_ack=True)
            ok = bool(method_frame)
            if ok:
                messages.append(body)

        connection.close()

        return messages

    def _get_connection_and_channel(self, passive=False):
        credentials = pika.PlainCredentials("admin", "password")
        parameters = pika.ConnectionParameters("rabbitmq", 5672, "/", credentials)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue="items", passive=passive)
        return connection, channel

