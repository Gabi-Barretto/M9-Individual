# Consumer e Producer - Confluent Kafka

A solução apresenta dois scripts distintos que interagem com o Apache Kafka, um sistema distribuído de mensagens e streaming de eventos. Cada script inclui uma função `read_config` para ler as configurações de conexão com o Kafka de um arquivo chamado `client.properties`, além de operações distintas de produção e consumo de mensagens.

Vídeo demonstrativo no [Drive](https://drive.google.com/file/d/1D7f81iwstToIGgQQp4uthuDZPnr8GCco/view?usp=sharing)

### Compreendendo o Apache Kafka
O Apache Kafka é uma plataforma de streaming de eventos distribuída que permite publicar, armazenar, processar e consumir fluxos de registros (mensagens) em tempo real. No contexto desses scripts, o Kafka é utilizado para produzir (enviar) e consumir (receber) mensagens de um tópico especificado. Tópicos no Kafka são categorias ou feeds nomeados para os quais as mensagens são publicadas.

### Primeiro Script: Produção e Consumo de Mensagens

#### Configuração (Função `read_config`)
- **Propósito:** Carrega as configurações necessárias para a conexão com o Kafka a partir de um arquivo externo (`client.properties`). Isso permite modularizar a configuração e facilitar mudanças sem a necessidade de alterar o código.
- **Funcionamento:** Abre o arquivo especificado, lê cada linha não vazia que não comece com "#", e divide cada linha em chave e valor pela primeira ocorrência do caractere "=". Os valores são armazenados em um dicionário `config`, que é retornado.

#### Produção de Mensagens
- **Inicialização do Producer:** Utiliza as configurações carregadas para criar uma instância do `Producer`. Esse produtor é responsável por enviar mensagens ao Kafka.
- **Envio de Mensagem:** A função `produce` do produtor é chamada para enviar uma mensagem com uma chave (`key`) e um valor (`value`) ao tópico `topic_teste`. Após isso, `producer.flush()` é chamado para garantir que todas as mensagens pendentes sejam enviadas.

#### Consumo de Mensagens
- **Configuração do Consumidor:** Modifica o dicionário de configuração adicionando um `group.id` (identificador para o grupo de consumidores) e `auto.offset.reset` (define de onde começar a consumir mensagens no tópico).
- **Inicialização do Consumer e Inscrição no Tópico:** Cria uma instância do `Consumer` com as configurações e se inscreve no tópico `topic_teste`.
- **Loop de Consumo:** Entra em um loop infinito, consumindo mensagens com `consumer.poll(1.0)`. Para cada mensagem válida recebida (sem erro), decodifica e imprime sua chave e valor. O loop pode ser interrompido manualmente, e o consumidor é fechado no final.

### Segundo Script: Produção de Mensagens com Dados de Sensores

#### Produção de Mensagens
- **Preparação da Mensagem:** Define um dicionário que representa os dados de um sensor, incluindo um identificador, carimbo de data/hora, tipo de poluente e nível. Este dicionário é convertido para uma string JSON e, em seguida, para bytes.
- **Envio de Mensagens:** Em um loop, o script produz a mesma mensagem JSON cinco vezes, enviando-a ao Kafka no tópico `topic_teste` com a chave `key`. Cada mensagem é potencialmente destinada a ser processada por um consumidor, simulando o envio de dados de sensores em intervalos ou eventos.
- **Finalização:** Assim como no primeiro script, `producer.flush()` é chamado ao final para garantir o envio de todas as mensagens.

### Testes

Realizei um teste de integridade dos dados, porém não consegui mapear corretamente o assert, caindo em erro. Mas acredito que a estrutura está próxima da correta.

### Considerações Finais

Ambos os scripts exemplificam o uso básico mas fundamental do Apache Kafka em cenários de produção e consumo de mensagens. O primeiro oferece uma visão abrangente do ciclo de vida das mensagens no Kafka, cobrindo tanto a produção quanto o consumo. O segundo foca na simulação de um caso de uso comum de Kafka: o envio de dados de dispositivos ou sensores para processamento e análise em tempo real.