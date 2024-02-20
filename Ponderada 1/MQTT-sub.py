import json
import random
from paho.mqtt import client as mqtt_client

broker = 'broker.hivemq.com'
port = 8883
# Lista de tópicos para subscrição ou uso de wildcard
topics = [("meuTesteIoT/sensor/radiacao_solar", 0), ("meuTesteIoT/sensor/temperatura", 0)]
client_id = f'python-mqtt-{random.randint(0, 1000)}'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker as Subscriber!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client()
    client.on_connect = on_connect
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        message = json.loads(msg.payload.decode())
        print(f"Received `{message}` from `{msg.topic}` topic")

    client.subscribe(topics)  # Subscrevendo a múltiplos tópicos
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()
