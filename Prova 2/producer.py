from confluent_kafka import Producer, Consumer
import json

def read_config():
  config = {}
  with open("client.properties") as fh:
    for line in fh:
      line = line.strip()
      if len(line) != 0 and line[0] != "#":
        parameter, value = line.strip().split('=', 1)
        config[parameter] = value.strip()
  return config

config = read_config()

producer = Producer(config)

topic = 'topic_teste'
key = "key" 

message = {
  
    "idSensor": "sensor_001",
    "timestamp": "2024-04-04T12:34:56Z",
    "tipoPoluente": "PM2.5",
    "nivel": 35.2
}

bytes_para_enviar = json.dumps(message).encode('utf-8')

for i in range(5):

    producer.produce(topic, key=key, value=bytes_para_enviar)
    print(f"Produced message to topic {topic}: key = {key:12} value = {i:12}")

# Fecha a conexão com o Kafka
producer.flush()


