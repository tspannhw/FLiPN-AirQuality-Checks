# FLiPN-AirQuality-Checks

FLiPN - Air Quality - Checks against MQTT, Kafka, AMQP/RabbitMQ.  MoP. KoP. AoP.


## Build 

````

bin/pulsar-admin topics create persistent://public/default/__amqp_queue__amqp-airquality

bin/pulsar-client consume "persistent://public/default/__amqp_queue__amqp-airquality"

```

## Configuration

````
#### --- MQTT-on-Pulsar MoP

# https://hub.streamnative.io/protocol-handlers/mop/0.2.0
# messaging protocol for mqtt,kafka
messagingProtocols=mqtt,amqp,kafka
# ,kafka

# directory
protocolHandlerDirectory=./protocols

#mqtt 3.1.1
# port / ip
mqttListeners=mqtt://127.0.0.1:1883
advertisedAddress=127.0.0.1
#advertisedAddress=192.168.1.181
#127.0.0.1 0.0.0.0 192.168.1.181

### --- MQTT-on-Pulsar MoP (end)

### --- AMQP
# add amqp configs

amqpListeners=amqp://127.0.0.1:5672
amqpTenant=public
### --- End of AoP
#
### --- Kafka-on-Pulsar KoP

allowAutoTopicCreationType=partitioned
# Use `kafkaListeners` here for KoP 2.8.0 because `listeners` is marked as deprecated from KoP 2.8.0
kafkaListeners=PLAINTEXT://0.0.0.0:9092
# This config is not required unless you want to expose another address to the Kafka client.
# If it’s not configured, it will be the same with `kafkaListeners` config by default
kafkaAdvertisedListeners=PLAINTEXT://0.0.0.0:9092
brokerEntryMetadataInterceptors=org.apache.pulsar.common.intercept.AppendIndexMetadataInterceptor
brokerDeleteInactiveTopicsEnabled=false    # !! overrides the default setting !!
#kafkaTransactionCoordinatorEnabled=true 
kafkaTenant=kop
kafkaNamespace=kop

````

### In Protocol directory 

pulsar-protocol-handler-amqp-2.9.1.2.nar

### References

* https://pika.readthedocs.io/en/stable/examples/blocking_consume.html
* https://github.com/tspannhw/FLiPN-AirQuality-REST
