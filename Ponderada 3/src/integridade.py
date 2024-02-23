import paho.mqtt.publish as publish

# Substitua pelos valores apropriados
broker_address = "broker.hivemq.com"  # Endereço do broker MQTT
port = 1883  # Porta padrão do MQTT (sem SSL/TLS)
topic = "meuTesteIoT/sensor/temperatura"  # Tópico onde a mensagem será publicada
message = "oioi"  # Conteúdo da mensagem

try:
    # Publicando a mensagem
    publish.single(topic, message, hostname=broker_address, port=port)
    print(f"Mensagem '{message}' enviada para o tópico '{topic}' com sucesso.")
except Exception as e:
    print(f"Erro ao enviar mensagem: {e}")