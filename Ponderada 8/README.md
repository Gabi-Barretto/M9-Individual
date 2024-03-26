# Simulador de Dispositivos IoT com HiveMQ, Kafka, MongoDB e Visualização de Dados

Este projeto implementa um fluxo de dados completo para simulação de dispositivos IoT, utilizando o broker MQTT HiveMQ para a comunicação dos dispositivos, Confluent Kafka para o processamento e roteamento de mensagens, MongoDB para armazenamento dos dados, e uma ferramenta de visualização (como Metabase ou outra de sua escolha) para análise dos dados armazenados.

- Em [Mídia](https://github.com/Gabi-Barretto/M9-Individual/tree/main/Ponderada%208/M%C3%ADdia) temos o vídeo do funcionamento. Tambem no disponível no [Drive](https://drive.google.com/file/d/1YcyzOI-JyVa-AQy5F7QoXj69M-kOpAh8/view?usp=sharing).

## Componentes do Projeto

- **Publisher (`publisher.py`):** Simula dispositivos IoT enviando dados para um tópico MQTT no HiveMQ.
- **HiveMQ:** Broker MQTT que recebe as mensagens dos dispositivos simulados.
- **Confluent Kafka:** Plataforma de streaming de dados que se inscreve nos tópicos MQTT do HiveMQ e armazena as mensagens recebidas.
- **Subscriber (`subscriber.py`):** Consome as mensagens do tópico Kafka, processando e encaminhando para uma API REST.
- **API REST (`api.py`):** Recebe dados do Kafka (via subscriber) e os insere no MongoDB.
- **MongoDB:** Banco de dados NoSQL que armazena os dados recebidos para análise futura.
- **Ferramenta de Visualização de Dados:** Utilizada para conectar ao MongoDB e visualizar os dados coletados (Metabase recomendado).

## Configuração e Instalação

### Requisitos

- Python 3.6 ou superior.
- Conta no MongoDB Atlas para hospedar o banco de dados.
- Acesso a um broker HiveMQ e uma instância Confluent Kafka.
- Docker para rodar o Metabase (opcional).

### Instalação

1. **Dependências Python:**

   Instale as bibliotecas necessárias (Paho MQTT, Flask, PyMongo, dotenv, Confluent Kafka Python):

   ```bash
   pip install paho-mqtt flask pymongo python-dotenv confluent-kafka
   ```

2. **Configuração do Ambiente (.env):**

   Configure as variáveis de ambiente necessárias para a conexão com o HiveMQ, Kafka e MongoDB no arquivo `.env`:

   ```env
   BROKER_ADDR="endereco_do_broker_mqtt"
   PORT=1883 # ou outra porta, conforme configurado no seu broker MQTT
   TOPIC="nome_do_topico_mqtt"
   HIVE_USER="seu_usuario"
   HIVE_PSWD="sua_senha"
   KAFKA_CONFIG="caminho_para_o_arquivo_client.properties"
   MONGO_URL="string_de_conexao_do_mongodb"
   ```

3. **MongoDB Atlas:**

   Crie seu cluster no MongoDB Atlas e obtenha a string de conexão.

4. **Metabase:**

   Se desejar utilizar o Metabase para visualização:

   ```bash
   docker pull metabase/metabase
   docker run -d -p 3000:3000 --name metabase metabase/metabase
   ```

## Execução

1. **Inicie a API Flask:** Execute `api.py` para lançar a API que insere dados no MongoDB.

   ```bash
   python api.py
   ```

2. **Subscriber Kafka:** Inicie `subscriber.py` para consumir mensagens do Kafka e enviar para a API.

   ```bash
   python subscriber.py
   ```

3. **Publisher MQTT:** Execute `publisher.py` para simular a publicação de dados dos dispositivos IoT ao HiveMQ.

   ```bash
   python publisher.py
   ```

## Visualização de Dados

Após os dados serem inseridos no MongoDB, utilize o Metabase (ou outra ferramenta de sua escolha) para criar dashboards e visualizações dos dados coletados dos dispositivos IoT.

## Notas

Certifique-se de que a ponte ou conexão entre o [HiveMQ](https://console.hivemq.cloud/) e o [Kafka](https://confluent.cloud/home), realizado em **integrations** dentro do cluster, esteja corretamente configurada para permitir o fluxo de mensagens entre os sistemas. Revise todas as configurações relacionadas para garantir a comunicação efetiva entre os componentes do projeto. 
