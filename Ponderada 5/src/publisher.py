import paho.mqtt.client as paho
import os
from dotenv import load_dotenv
import time

load_dotenv()  # Carrega variáveis de ambiente do arquivo .env

# Configurações do broker
broker_address = os.getenv("BROKER_ADDR")
port = int(os.getenv("PORT", "8883"))
topic = os.getenv("TOPIC", "my/test/topic")
username = os.getenv("HIVE_USER")
password = os.getenv("HIVE_PSWD")

def on_publish(client, userdata, mid, *args, **kwargs):
    print("Data published \n")
    pass

client = paho.Client(paho.CallbackAPIVersion.VERSION2, "Publisher", protocol=paho.MQTTv5)
client.username_pw_set(username, password)
client.on_publish = on_publish

client.tls_set()

client.connect(broker_address, port=port)
client.loop_start()

while True:
    message = input("Enter message to publish or type 'exit' to quit:\n")
    if message.lower() == 'exit':
        break
    result = client.publish(topic, message)
    status = result[0]
    if status == 0:
        print(f"Sent '{message}' to topic '{topic}'")
    else:
        print(f"Failed to send message to topic {topic}")
    time.sleep(1)

client.loop_stop()
