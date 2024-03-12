import paho.mqtt.client as paho
from paho import mqtt
import os
import requests
from dotenv import load_dotenv

load_dotenv() # Carrega variáveis de ambiente do arquivo .env

# Configurações do broker
broker_address = os.getenv("BROKER_ADDR")
port = int(os.getenv("PORT", "8883"))
topic = os.getenv("TOPIC", "my/test/topic")
username = os.getenv("HIVE_USER")
password = os.getenv("HIVE_PSWD")
api_url = os.getenv("API_URL", "http://localhost:5000/data")

def on_connect(client, userdata, flags, rc, properties):
    print(f"CONNACK received with code {rc}")
    client.subscribe(topic, qos=1)

def on_message(client, userdata, msg):
    print(f"{msg.topic} (QoS: {msg.qos}) - {msg.payload.decode('utf-8')}")
    # Envia os dados para a API
    response = requests.post(api_url, json={"valor": msg.payload.decode()})
    print(f"Response from API: {response.text}")

client = paho.Client(paho.CallbackAPIVersion.VERSION2, "Subscriber", protocol=paho.MQTTv5)
client.on_connect = on_connect
client.on_message = on_message

client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set(username, password)

client.connect(broker_address, port=port)
client.loop_forever()
