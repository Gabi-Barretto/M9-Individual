# Simulador de Dispositivos IoT

Este projeto desenvolve um simulador de dispositivos IoT focado na simulação de um sensor de radiação solar, especificamente o modelo HoboNet RXW-LIB-900. O simulador é capaz de gerar e enviar mensagens MQTT que simulam as leituras de radiação solar deste dispositivo.

Em [Mídia](https://github.com/Gabi-Barretto/M9-Individual/tree/main/Ponderada/M%C3%ADdia) temos o vídeo do funcionamento do publisher e seus testes em GO.

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

- `MQTT-pub.py`: Simula o dispositivo IoT enviando dados de radiação solar.
- `testes.go`: Construido para automatizar a realização de testes de nosso Publisher.

### Executando o MQTT-Pub

Para simular o envio de dados de radiação solar, execute:

```bash
python MQTT-pub.py
```

Este script irá gerar e enviar uma mensagem MQTT em intervalos regulares (por exemplo, a cada 15 minutos), simulando as leituras do sensor de radiação solar.

### Executando o teste em GO

- Instalar Go: Certifique-se de que Go está instalado em sua máquina. Pode ser baixado de golang.org.
- Instalar MQTT Client: Você precisa instalar a biblioteca MQTT para Go, que pode ser feita executando go get github.com/eclipse/paho.mqtt.golang no terminal.
- Escrever o Script: Use o código fornecido acima como um ponto de partida. Salve-o em um arquivo com a extensão .go.
- Executar o Script: Navegue até o diretório onde o arquivo .go está salvo e execute go run <nome_do_arquivo>.go no terminal. 

```bash

(go run testes.go)

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

As evidências de funcionamento são apresentadas através de capturas de tela ou logs que mostram o correto envio e recebimento de mensagens entre o MQTT-pub e o MQTT-sub. (Incluir evidências conforme disponível).

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
