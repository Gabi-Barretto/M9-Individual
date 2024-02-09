import csv
import time
import json
from paho.mqtt import client as mqtt_client

broker = 'broker.hivemq.com'
port = 8000
client_id = "clientId-Qro3K1kRhV"
csv_file_path = "Ponderada 1\data\sensors.csv"

def read_sensor_data_from_csv(csv_path):
    while True:  # Loop infinito para simular dados contínuos
        with open(csv_path, mode='r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                yield row
        # Opcional: Pode-se adicionar uma pausa ou condição de saída aqui

# Criar um gerador
sensor_data_generator = read_sensor_data_from_csv(csv_file_path)

def generate_data(sensor_name):
    row = next(sensor_data_generator)  # Pega a próxima linha de dados do gerador
    return row[sensor_name]

# Configurações dos sensores utilizando o gerador para dados
sensores = {
    "radiacao_solar": {
        "topic": "meuTesteIoT/sensor/radiacao_solar",
        "generate_data": lambda: generate_data("radiacao_solar")
    },
    "temperatura": {
        "topic": "meuTesteIoT/sensor/temperatura",
        "generate_data": lambda: generate_data("temperatura")
    },
    # Adicione mais sensores conforme necessário, correspondendo às colunas do CSV
}

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
        for sensor_name, sensor_info in sensores.items():
            msg = json.dumps({"value": sensor_info["generate_data"]()})
            result = client.publish(sensor_info["topic"], msg)
            status = result[0]
            if status == 0:
                print(f"Sent `{msg}` to topic `{sensor_info['topic']}`")
            else:
                print(f"Failed to send message to topic {sensor_info['topic']}")
            time.sleep(1)  # Ajuste o tempo de espera conforme necessário

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == "__main__":
   run()
