### Resolução do Desafio: Manipulação de Arquivos Parquet em Python

#### 1. Instalando Dependências
Certifique-se de ter o Python instalado em seu sistema. Você também precisa ter a biblioteca `pandas` instalada. Se você ainda não tiver o `pandas`, pode instalá-lo usando o pip:

```bash
pip install pandas
```

#### 2. Resolução do Desafio

##### 2.1. Calcular Estatísticas de um Arquivo Parquet
Para calcular as estatísticas de um arquivo Parquet, seguimos estas etapas:

1. **Importar a Biblioteca Pandas**: Importamos a biblioteca `pandas` para manipular o arquivo Parquet.
   
2. **Definir uma Função para Calcular Estatísticas**: Criamos uma função `calcular_estatisticas_parquet(nome_arquivo)` que aceita o nome do arquivo Parquet como entrada.

3. **Ler o Arquivo Parquet**: Usamos `pd.read_parquet(nome_arquivo)` para ler o arquivo Parquet e carregá-lo em um DataFrame.

4. **Calcular as Estatísticas**: Usamos métodos do DataFrame do `pandas` para calcular o mínimo, o máximo e a média dos valores.

5. **Retornar as Estatísticas**: A função retorna os valores mínimos, máximos e médios.

##### 2.2. Converter um Arquivo de Texto para Parquet
Para converter um arquivo de texto para Parquet, seguimos estas etapas:

1. **Importar a Biblioteca Pandas**: Mais uma vez, importamos a biblioteca `pandas`.

2. **Definir uma Função para Conversão**: Criamos uma função `converter_txt_para_parquet(arquivo_txt, nome_arquivo_parquet)` que aceita o nome do arquivo de texto e o nome do arquivo Parquet de destino.

3. **Ler o Arquivo de Texto**: Usamos `pd.read_csv(arquivo_txt, delimiter='\t')` para ler o arquivo de texto, assumindo que os valores são separados por tabulação. Você pode ajustar o delimitador conforme necessário.

4. **Salvar como Arquivo Parquet**: Usamos o método `to_parquet()` para salvar o DataFrame como um arquivo Parquet.