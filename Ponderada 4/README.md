# Simulador de Dispositivos IoT

Este projeto desenvolve um simulador de dispositivos IoT focado na simulação de um sensor de radiação solar, especificamente o modelo HoboNet RXW-LIB-900, e temperatura. O simulador é capaz de gerar e enviar mensagens MQTT que simulam as leituras destes dispositivos.

**Agora** o script conta com TLS. Colocar TLS (Transport Layer Security) em um MQTT (Message Queuing Telemetry Transport) Publisher é uma prática recomendada para melhorar a segurança na comunicação entre o cliente (publisher) e o servidor (broker) MQTT. TLS é um protocolo de segurança que fornece comunicação criptografada e autenticação segura na Internet com isso, assegura-se que os dados transmitidos entre o publisher e o broker sejam criptografados, protegendo assim contra interceptações e ataques man-in-the-middle.

- Em [Mídia](https://github.com/Gabi-Barretto/M9-Individual/tree/main/Ponderada%204/M%C3%ADdia) temos o vídeo do funcionamento do publisher e seu subscriber mosquitto. Tambem no disponível no [Drive](https://drive.google.com/file/d/1663MNgkfRqDzEjzu2D4ZOunRVjjokaAi/view?usp=sharing).

- Também temos seus [testes em go](https://drive.google.com/file/d/1RkEWG9Vkn9Dw_MGqFHbuCOnynU3RcIc4/view?usp=sharing) em funcionamento.

## Requisitos

- Python 3.x
- paho-mqtt

## Instalação

Para utilizar este simulador, é necessário instalar a biblioteca `paho-mqtt` na versão 1.6.1. A nova versão pode necessitar mudanças no Script. 
Isso pode ser feito através do comando:

```bash
pip install paho-mqtt==1.6.1
```

## Uso

O projeto consiste em dois scripts principais:

- `MQTT-pub.py`: Simula o dispositivo IoT enviando dados de radiação solar e temperatura.

### Executando o MQTT-Pub

Para simular o envio de dados, execute:

```bash
python MQTT-pub.py
```

Este script irá gerar e enviar uma mensagem MQTT em intervalos regulares (por exemplo, a cada 15 minutos), simulando as leituras do sensor de radiação solar.

### Executando o teste em GO

- Instalar Go: Certifique-se de que Go está instalado em sua máquina. Pode ser baixado de golang.org. (Lembrar de adicionar ao ~./bashrc ou ~./person)
- Instalar MQTT Client: Você precisa instalar a biblioteca MQTT para Go, que pode ser feita executando go get github.com/eclipse/paho.mqtt.golang no terminal.
- Criar um Módulo Go: Navegue até o diretório onde você deseja criar seu projeto Go.
- Execute para criar um novo módulo. Isso criará um arquivo go.mod no seu diretório, que é usado para gerenciar suas dependências.

```bash
go mod init <nome_do_seu_projeto>  
```

- Após inicializar seu módulo, você pode adicionar dependências executando o comando abaixo. Isso irá baixar a biblioteca MQTT e atualizar o arquivo go.mod com a versão específica da dependência.

```bash
go get github.com/eclipse/paho.mqtt.golang@latest. 
```

- Para construir seu projeto, execute o comando abaixo dentro do diretório do seu projeto. Isso compilará seu código e gerará um executável.

```bash
go build 
```

- Executar o Script: Navegue até o [diretório](https://github.com/Gabi-Barretto/M9-Individual/tree/main/Ponderada/src/Teste_em_GO) onde o arquivo .go está salvo e execute  o comando abaixo no terminal.

```bash
cd Documents/Git/M9-Individual/Ponderada/src/Teste_em_GO

go run testes.go
```

- Testar Contra o Script Python: Execute o script Python e o script Go simultaneamente. O script Go deve receber e imprimir as mensagens publicadas pelo script Python.


## Estrutura da Mensagem

As mensagens enviadas pelo simulador possuem o seguinte formato JSON:

```json
{
  "sensor": "Sensor de Temperatura Ambiente",
  "valor": 1200.5,
  "unidade": "W/m²",
  "timestamp": "datetime.now()"
}
```

- `sensor_id`: Identificador do sensor.
- `medicao`: Valor simulado da radiação solar.
- `unidade`: Unidade de medida da radiação (Watts por metro quadrado).

## Evidências de Funcionamento

As evidências de funcionamento são apresentadas através de capturas de tela ou logs que mostram o correto envio e recebimento de mensagens entre o MQTT-pub e o teste em GO.

Em [Mídia](https://github.com/Gabi-Barretto/M9-Individual/tree/main/Ponderada/M%C3%ADdia) temos o vídeo do funcionamento do publisher e seus testes em GO.

## Extensibilidade

O sistema foi projetado com abstrações que permitem a fácil adaptação para simular outros dispositivos IoT além dos sensores de radiação solar e temperatura especificados. 

Para adicionar um novo tipo de dispositivo, é necessário:

- Adicionar um novo sensor ao dicionário "sensores".

```
sensores = {
    "radiacao_solar": {
        "topic": "meuTesteIoT/sensor/radiacao_solar",
        "generate_data": lambda: generate_data("radiacao_solar")
    },
    "temperatura": {
        "topic": "meuTesteIoT/sensor/temperatura",
        "generate_data": lambda: generate_data("temperatura")
    },
    # Adicione mais sensores conforme necessário, correspondendo às colunas do CSV...
}
```

- Atualizar o CSV com o nome e dados devidamente em conformidade com o Script.

Este design facilita a extensão do simulador para abranger uma ampla variedade de dispositivos IoT sem necessidade de refatoração substancial.

## Conclusão

Este simulador oferece uma ferramenta valiosa para o desenvolvimento e teste de aplicações IoT, permitindo a simulação realista de dispositivos e a geração de dados para análise. Através de sua extensibilidade, o simulador pode ser adaptado para uma ampla gama de dispositivos IoT, tornando-o uma solução versátil para diversos cenários de simulação.
