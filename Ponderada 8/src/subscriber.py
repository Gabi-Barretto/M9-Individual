from confluent_kafka import Producer, Consumer
import requests 


def read_config():
  # reads the client configuration from client.properties
  # and returns it as a key-value map
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
  
  # creates a new producer instance
  producer = Producer(config)

  # produces a sample message
  key = "key"
  value = "value"
  producer.produce(topic, key=key, value=value)
  print(f"Produced message to topic {topic}: key = {key:12} value = {value:12}")
  
  # send any outstanding or buffered messages to the Kafka broker
  producer.flush()

  # sets the consumer group ID and offset  
  config["group.id"] = "python-group-1"
  config["auto.offset.reset"] = "earliest"

  # creates a new consumer and subscribes to your topic
  consumer = Consumer(config)
  consumer.subscribe([topic])
  try:
    while True:
      # consumer polls the topic and prints any incoming messages
      msg = consumer.poll(1.0)
      if msg is not None and msg.error() is None:
        key = msg.key().decode("utf-8")
        value = msg.value().decode("utf-8")
        print(f"Received message: {msg.value().decode('utf-8')}")
        # Supondo que a sua API esteja rodando na porta padrão localhost:5000
        response = requests.post('http://localhost:5000/data', json={"valor": value})
        print(f"API Response: {response.json()}")
  except KeyboardInterrupt:
    pass
  finally:
    # closes the consumer connection
    consumer.close()


main()