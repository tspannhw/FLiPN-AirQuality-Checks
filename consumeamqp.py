import pika

def on_message(channel, method_frame, header_frame, body):
    print(method_frame.delivery_tag)
    print(body)
    print()
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)

parms = pika.URLParameters('amqp://pulsar1:5672/')
connection = pika.BlockingConnection(parms)

channel = connection.channel()
channel.basic_consume('amqp-airquality', on_message)
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
connection.close()
