from confluent_kafka import Producer, Consumer, KafkaError
import json

def read_config(file_path="../client.properties"):
    config = {}
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split("=", 1)
                config[key.strip()] = value.strip()
    return config

def produce_message(config, topic, message):
    producer = Producer(config)
    def delivery_report(err, msg):
        if err is not None:
            print(f"Message delivery failed: {err}")
        else:
            print(f"Message {message} delivered to {msg.topic()} [{msg.partition()}]")

    bytes_para_enviar = json.dumps(message).encode('utf-8')

    producer.produce(topic, key="key", value=bytes_para_enviar, callback=delivery_report)
    producer.flush()

def consume_message(config, topic):
    config["group.id"] = "python-group-1"
    config["auto.offset.reset"] = "earliest"
    consumer = Consumer(config)
    consumer.subscribe([topic])

    try:
        msg = consumer.poll(1.0)
        if msg is not None and msg.error() is None:
            print(f"Received message: {msg.value().decode('utf-8')}")
            return json.encodermsg.value().decode('utf-8')
    finally:
        consumer.close()
    

config = read_config()
topic = "topic_teste"
message = {"id": 1, "content": "Test Message"}

produce_message(config, topic, message)

received_message = consume_message(config, topic)
assert message == received_message, "Integrity Test Failed: Sent message not received correctly."

print("Integrity Test Passed: Sent message received correctly.")
