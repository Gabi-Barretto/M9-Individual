# Simulador de Dispositivos IoT com Paho MQTT 2.0 e Metabase

Este projeto implementa um simulador de dispositivos IoT, utilizando a versão 2.0 da biblioteca Paho MQTT para simular a publicação e subscrição de mensagens MQTT. O projeto é composto por um publisher MQTT que simula a geração de dados de dispositivos (por exemplo, sensores de temperatura ou radiação solar) e um subscriber MQTT que recebe essas mensagens. Uma API em Flask é usada para inserir as mensagens recebidas em um banco de dados MongoDB, demonstrando um fluxo de dados do dispositivo IoT para armazenamento de dados que serão apresentados e manipulados via Metabase.

- Em [Mídia](https://github.com/Gabi-Barretto/M9-Individual/tree/main/Ponderada%207/M%C3%ADdia) temos o vídeo do funcionamento. Tambem no disponível no [Drive](https://drive.google.com/file/d/1Ko2Yto1zTyR2htdeLDOGYhtZ8V-TL3ZV/view?usp=sharing).

## Requisitos

- Python 3.6 ou superior
- Paho MQTT 2.0
- Flask
- pymongo

## Instalação

### Bibliotecas Python

Instale as dependências necessárias utilizando pip:

```bash
pip install paho-mqtt==2.0.0 flask pymongo
```

### Configuração do Ambiente

Crie um arquivo `.env` na raiz do projeto para armazenar as configurações sensíveis e específicas do ambiente, como segue:

```env
# Configurações do MQTT Broker
BROKER_ADDR=<endereco_do_broker>
PORT=8883
TOPIC=<topico_mqtt>
HIVE_USER=<usuario_mqtt>
HIVE_PSWD=<senha_mqtt>

# URL da API do mongodb para o subscriber enviar dados
API_URL=<sua_conexão_mongodb>
```

Substitua os placeholders pelas suas informações de configuração.

## Estrutura do Projeto

- `publisher.py`: Script que simula um dispositivo IoT, publicando mensagens em um tópico MQTT.
- `subscriber.py`: Script que se inscreve em um tópico MQTT, recebendo mensagens e enviando-as para uma API Flask.
- `api.py`: API Flask que recebe dados do subscriber via HTTP POST e os insere em um banco de dados Mongodb.

## Execução

### Banco de dados

Crie um cluster e banco de dados no MongoDB.

### API Flask

Inicie a API primeiro para garantir que o subscriber possa encaminhar as mensagens corretamente:

```bash
python3 api.py
```

### Subscriber MQTT

Em um novo terminal, inicie o subscriber:

```bash
python3 subscriber.py
```

### Publisher MQTT

Finalmente, em outro terminal, execute o publisher para começar a enviar mensagens:

```bash
python3 publisher.py
```

Digite as mensagens conforme solicitado pelo script do publisher. Essas mensagens serão enviadas ao tópico MQTT, recebidas pelo subscriber e então encaminhadas para a API, que as insere no banco de dados.

### Metabase

Para instalar o metabase e iniciar o container docker em localhost para utiliza-lo, faça:

```bash
docker pull metabase/metabase:latest
```
e em seguida,

```bash
docker run -d -p 3005:3000 -v ~/metabase:/metabase.db -v ~/juninho:/juninho --name metabase metabase/metabase
```

## Importância da Paho MQTT 2.0

A escolha da versão 2.0 da biblioteca Paho MQTT é crucial devido a melhorias significativas e novas funcionalidades introduzidas, tais como:

- Suporte aprimorado para o protocolo MQTT 5.0.
- Melhorias nas funções de callback, permitindo um manuseio mais eficiente das mensagens.
- Otimizações de desempenho e segurança.

Utilizar a versão 2.0 garante que o simulador de dispositivos IoT possa aproveitar essas melhorias para uma simulação mais eficaz e segura de dispositivos IoT.

## Conclusão

Este projeto demonstra a implementação de um fluxo de dados IoT completo, desde a geração de dados por dispositivos simulados até o armazenamento desses dados em um banco de dados não relacional disponibilizado no Metabase, utilizando o protocolo MQTT. A utilização da versão 2.0 da biblioteca Paho MQTT é fundamental para o sucesso deste projeto, oferecendo recursos avançados e melhorias essenciais.
