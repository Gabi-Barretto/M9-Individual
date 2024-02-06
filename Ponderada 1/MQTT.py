import random
import time
import json
from paho.mqtt import client as mqtt_client

broker = 'localhost'
port = 1883
topic = "iot/sensor/radiacao_solar"
client_id = f'python-mqtt-{random.randint(0, 1000)}'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
    while True:
        time.sleep(900)  # Simula a taxa de transmissão de 15 minutos
        message = {
            "sensor_id": "RXW-LIB-900",
            "medicao": random.uniform(0, 2000),  # Gera um valor aleatório dentro da faixa de medição
            "unidade": "W/m²"
        }
        message_json = json.dumps(message)
        result = client.publish(topic, message_json)
        status = result[0]
        if status == 0:
            print(f"Send `{message_json}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()
