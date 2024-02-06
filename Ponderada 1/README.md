# Simulador de Dispositivos IoT

Este projeto desenvolve um simulador de dispositivos IoT focado na simulação de um sensor de radiação solar, especificamente o modelo HoboNet RXW-LIB-900. O simulador é capaz de gerar e enviar mensagens MQTT que simulam as leituras de radiação solar deste dispositivo.

## Requisitos

- Python 3.x
- paho-mqtt

## Instalação

Para utilizar este simulador, é necessário instalar a biblioteca `paho-mqtt`. Isso pode ser feito através do comando:

```bash
pip install paho-mqtt
```

## Uso

O projeto consiste em dois scripts principais:

- `MQTT-pub.py`: Simula o dispositivo IoT enviando dados de radiação solar.
- `MQTT-sub.py`: Recebe e exibe os dados enviados pelo simulador.

### Executando o MQTT-Pub

Para simular o envio de dados de radiação solar, execute:

```bash
python MQTT-pub.py
```

Este script irá gerar e enviar uma mensagem MQTT em intervalos regulares (por exemplo, a cada 15 minutos), simulando as leituras do sensor de radiação solar.

### Executando o MQTT-Sub

Para receber e visualizar os dados enviados pelo MQTT-pub, execute em outro terminal:

```bash
python MQTT-sub.py
```

## Estrutura da Mensagem

As mensagens enviadas pelo simulador possuem o seguinte formato JSON:

```json
{
  "sensor_id": "RXW-LIB-900",
  "medicao": 1200.5,
  "unidade": "W/m²"
}
```

- `sensor_id`: Identificador do sensor.
- `medicao`: Valor simulado da radiação solar.
- `unidade`: Unidade de medida da radiação (Watts por metro quadrado).

## Evidências de Funcionamento

As evidências de funcionamento são apresentadas através de capturas de tela ou logs que mostram o correto envio e recebimento de mensagens entre o MQTT-pub e o MQTT-sub. (Incluir evidências conforme disponível).

## Extensibilidade

O sistema foi projetado com abstrações que permitem a fácil adaptação para simular outros dispositivos IoT além do sensor de radiação solar especificado. Para adicionar um novo tipo de dispositivo, é necessário:

- Implementar uma nova função de geração de dados que reflita as especificações do novo dispositivo.
- Configurar o `MQTT-pub.py` para usar essa nova função de geração de dados.

Este design facilita a extensão do simulador para abranger uma ampla variedade de dispositivos IoT sem necessidade de refatoração substancial.

## Conclusão

Este simulador oferece uma ferramenta valiosa para o desenvolvimento e teste de aplicações IoT, permitindo a simulação realista de dispositivos e a geração de dados para análise. Através de sua extensibilidade, o simulador pode ser adaptado para uma ampla gama de dispositivos IoT, tornando-o uma solução versátil para diversos cenários de simulação.
