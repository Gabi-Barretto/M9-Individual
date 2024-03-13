# Simulador de Dispositivos IoT com MQTT, MongoDB e Metabase

Este projeto simula o fluxo de dados de dispositivos IoT usando MQTT para comunicação entre dispositivos e um backend, Python com Flask para processar e armazenar esses dados em um MongoDB hospedado no Atlas, e Metabase para visualização e análise dos dados.

- Em [Mídia](https://github.com/Gabi-Barretto/M9-Individual/tree/main/Ponderada%207/M%C3%ADdia) temos o vídeo do funcionamento. Tambem no disponível no [Drive](https://drive.google.com/file/d/1Ko2Yto1zTyR2htdeLDOGYhtZ8V-TL3ZV/view?usp=sharing).

## Estrutura e Fluxo da Aplicação

1. **Publisher (publisher.py):** Simula dispositivos IoT enviando dados (por exemplo, leituras de sensores) para um tópico MQTT.
2. **Subscriber (subscriber.py):** Escuta o tópico MQTT para receber dados dos dispositivos e os encaminha para uma API REST.
3. **API REST (api.py):** Recebe os dados do subscriber e os insere no MongoDB, armazenando-os para análise posterior.
4. **MongoDB no Atlas:** Armazena os dados recebidos pela API REST, servindo como base de dados para análise.
5. **Metabase:** Ferramenta de visualização de dados conectada ao MongoDB no Atlas, permitindo a análise e visualização dos dados coletados.

## Configuração e Instalação

### Requisitos

- Python 3.6+
- MongoDB Atlas
- Metabase
- Bibliotecas Python: Paho MQTT, Flask, PyMongo, dotenv.

### Passos de Instalação

1. **Instalação das Dependências:**

   ```bash
   pip install paho-mqtt==2.0.0 flask pymongo python-dotenv
   ```

2. **Configuração do .env:**
   
   Crie um arquivo `.env` com as seguintes variáveis:
   
   ```env
   BROKER_ADDR="endereco_do_broker"
   PORT=8883
   TOPIC="topico_mqtt"
   HIVE_USER="usuario_mqtt"
   HIVE_PSWD="senha_mqtt"
   API_URL="sua_url_da_api"
   MONGO_URL="sua_string_de_conexao_mongodb"
   ```

3. **MongoDB Atlas:**

   Configure seu cluster no MongoDB Atlas e obtenha a string de conexão para seu banco de dados.

4. **Metabase:**

   ```bash
   docker pull metabase/metabase:latest
   docker run -d -p 3000:3000 --name metabase metabase/metabase
   ```

   Conecte o Metabase ao seu cluster do MongoDB Atlas seguindo as instruções na UI do Metabase.

## Execução

1. **API Flask:** Execute `api.py` para iniciar a API Flask que insere dados no MongoDB.
   
   ```bash
   python api.py
   ```

2. **Subscriber MQTT:** Execute `subscriber.py` para iniciar o subscriber que escuta o tópico MQTT.
   
   ```bash
   python subscriber.py
   ```

3. **Publisher MQTT:** Execute `publisher.py` para simular o envio de dados de dispositivos IoT.
   
   ```bash
   python publisher.py
   ```

## Visualização de Dados com Metabase

Após a inserção dos dados no MongoDB e conexão do mesmo com o Metabase, use-o para criar dashboards e visualizações dos dados coletados dos dispositivos IoT.

## Conclusão

Este projeto demonstra uma aplicação completa de IoT, desde a coleta de dados por dispositivos simulados até a visualização desses dados, utilizando tecnologias modernas como MQTT, Flask, MongoDB Atlas e Metabase.
