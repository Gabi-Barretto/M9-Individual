import csv
import time
import json
from datetime import datetime
import paho.mqtt.client as mqtt_client
import ssl

broker = 'mqtt.eclipseprojects.io'
port = 1883
username = "gabibarretto"
password = "DarthVader01"  # Substitua por sua senha real
csv_file_path = "Ponderada 1 e 2/src/data/sensors.csv"  # Ajuste o caminho do arquivo conforme seu ambiente 

def read_sensor_data_from_csv(csv_path):
    while True:  # Loop infinito para simular dados contínuos
        with open(csv_path, mode='r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                yield row
        # Opcional: Pode-se adicionar uma pausa ou condição de saída aqui

sensor_data_generator = read_sensor_data_from_csv(csv_file_path)

def generate_data(sensor_name):
    row = next(sensor_data_generator)  # Pega a próxima linha de dados do gerador
    return row[sensor_name]

sensores = {
    "radiacao_solar": {
        "topic": "meuTesteIoT/sensor/radiacao_solar",
        "generate_data": lambda: generate_data("radiacao_solar"),
        "unidade": "W/m²",
        "nome": "Sensor de Radiação Solar"
    },
    "temperatura_ambiente": {
        "topic": "meuTesteIoT/sensor/temperatura",
        "generate_data": lambda: generate_data("temperatura"),
        "unidade": "°C",
        "nome": "Sensor de Temperatura Ambiente"
    },
    # Adicione mais sensores conforme necessário
}

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client()
    #client.username_pw_set(username, password)  # Adicionando autenticação
    #client.tls_set()  # Habilitando TLS/SSL
    client.on_connect = on_connect
    client.connect(broker, port)
    client.loop_start()
    return client

def publish(client):
    while True:
        for sensor_name, sensor_info in sensores.items():
            valor = sensor_info["generate_data"]()
            mensagem = json.dumps({
                "sensor": sensor_info["nome"],
                "valor": valor,
                "unidade": sensor_info["unidade"],
                "timestamp": datetime.now().isoformat()
            })
            print(f"Sent `{mensagem}` to topic `{sensor_info['topic']}`")
            result = client.publish(sensor_info["topic"], mensagem)
            # Tratar o resultado da publicação como antes
            time.sleep(10)  # Ajuste o tempo de espera conforme necessário

def run():
    client = connect_mqtt()
    publish(client)

if __name__ == "__main__":
    run()
