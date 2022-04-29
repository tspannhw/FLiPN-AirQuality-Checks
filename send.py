    #### MQTT
    client.connect("pulsar1", 1883, 180)
    client.publish("persistent://public/default/mqtt-2", payload=json_string, qos=0, retain=True)

    #### AMQP/RabbitMQ
    parms = pika.URLParameters('amqp://pulsar1:5672/')
    connection = pika.BlockingConnection(parms)
    channel = connection.channel()

    try:
        channel.queue_declare("amqp-enviro")
        channel.basic_publish(exchange="", routing_key="amqp-enviro", body=json_string.encode('utf-8'))
    finally:
        connection.close()

    #### Kafka
    producer = KafkaProducer(bootstrap_servers='pulsar1:9092',retries=3)
    producer.send('rp4-kafka-1', json.dumps(row).encode('utf-8'))
