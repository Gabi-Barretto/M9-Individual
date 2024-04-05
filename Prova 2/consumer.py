from confluent_kafka import Producer, Consumer
import requests 

def read_config():
  config = {}
  with open("client.properties") as fh:
    for line in fh:
      line = line.strip()
      if len(line) != 0 and line[0] != "#":
        parameter, value = line.strip().split('=', 1)
        config[parameter] = value.strip()
  return config

def main():
  config = read_config()
  topic = "topic_teste"

  # Teste
  producer = Producer(config)

  key = "key"
  value = "value"
  producer.produce(topic, key=key, value=value)
  print(f"Produced message to topic {topic}: key = {key:12} value = {value:12}")
  
  producer.flush()

  config["group.id"] = "python-group-1"
  config["auto.offset.reset"] = "earliest"

  consumer = Consumer(config)
  consumer.subscribe([topic])
  try:
    while True:
      msg = consumer.poll(1.0)
      if msg is not None and msg.error() is None:
        key = msg.key().decode("utf-8")
        value = msg.value().decode("utf-8")
        print(f"Received message: {msg.value().decode('utf-8')}")

  except KeyboardInterrupt:
    pass
  finally:
    # closes the consumer connection
    consumer.close()

main()