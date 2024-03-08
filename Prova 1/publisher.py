import csv
import time
import json
from datetime import datetime
import paho.mqtt.client as mqtt_client
import ssl

broker = '9b6c1af8442543edbffca7a1864df2e3.s1.eu.hivemq.cloud'
port = 8883
# username = "rnicola"
# password = "cellarDoor1"  # Substitua por sua senha real
csv_file_path = "Prova 1/data.csv"  # Ajuste o caminho do arquivo conforme seu ambiente 

# def read_sensor_data_from_csv(csv_path):
#     while True:  # Loop infinito para simular dados contínuos
#         with open(csv_path, mode='r') as csvfile:
#             csvreader = csv.DictReader(csvfile)
#             for row in csvreader:
#                 yield row
#         # Opcional: Pode-se adicionar uma pausa ou condição de saída aqui

# sensor_data_generator = read_sensor_data_from_csv(csv_file_path)

# def generate_data(sensor_name):
#     row = next(sensor_data_generator)  # Pega a próxima linha de dados do gerador
#     return row[sensor_name]

def generate_alert(value, tipo):
    if tipo == "freezer":
        if value < -25:
            return "Alerta! Temperatura abaixo do limite."
        elif value > -15:
            return "Alerta! Temperatura acima do limite."
    elif tipo == "geladeira":
        if value < 2:
            return "Alerta! Temperatura abaixo do limite."
        elif value > 10:
            return "Alerta! Temperatura acima do limite."

sensores = {
    'freezer': 
    {
        'nome': 'freezer', 
        'topic': 'meuTesteIoT/sensor/freezer',
        'id': 'lj01f01',
        'tipo': 'freezer',
        'data': -10
    },
    'geladeira': 
    {
        'nome': 'geladeira',
        'topic': 'meuTesteIoT/sensor/geladeira',
        'id': '823edjs',
        'tipo': 'geladeira',
        'data': 10
    },
    'freezer1': 
    {
        'nome': 'freezer',
        'topic': 'meuTesteIoT/sensor/freezer',
        'id': 'lj01f01',
        'tipo': 'freezer',
        'data': -26
    },
    'geladeira1': 
    {
        'nome': 'geladeira1',
        'topic': 'meuTesteIoT/sensor/geladeira',
        'id': '823edjs',
        'tipo': 'geladeira',
        'data': 1
    }
    # Adicione mais sensores conforme necessário
}

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client()
    # client.username_pw_set(username, password)
    # client.tls_set(tls_version=ssl.PROTOCOL_TLS)
    client.on_connect = on_connect
    client.connect(broker, port)
    client.loop_start()
    return client

def publish(client):
    while True:
        for sensor_name, sensor_info in sensores.items():
            mensagem = json.dumps({
                "nome": sensor_name,
                "sensor": sensor_info["nome"],
                "id": sensor_info["id"],
                "tipo": sensor_info["tipo"],
                "data": sensor_info["data"],
                "timestamp": datetime.now().isoformat()
            })
            value = float(sensor_info["data"])
            if (-25 < value or value < -15 and sensor_info["tipo"] == "freezer") or (2 < value or value < 10 and sensor_info["tipo"] == "geladeira"):
                alerta = generate_alert(value, sensor_info["tipo"])
                print(f" {alerta} Sent `{mensagem}` to topic `{sensor_info['topic']}`")

            print(f"Sent `{mensagem}` to topic `{sensor_info['topic']}`")
            result = client.publish(sensor_info["topic"], mensagem)
            # Tratar o resultado da publicação como antes
            time.sleep(5)  # Ajuste o tempo de espera conforme necessário

def run():
    client = connect_mqtt()
    publish(client)

if __name__ == "__main__":
    run()
