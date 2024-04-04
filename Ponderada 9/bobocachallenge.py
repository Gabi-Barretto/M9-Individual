import pandas as pd

# Função para calcular min, max e média de um arquivo Parquet
def calcular_estatisticas_parquet(nome_arquivo):
    # Lendo o arquivo Parquet
    df = pd.read_parquet(nome_arquivo)
    
    # Identificando a única coluna com valores
    coluna = df.columns[1]  # Pega a primeira (e única) coluna
    
    # Calculando estatísticas para a coluna identificada
    min_valor = df[coluna].min()
    max_valor = df[coluna].max()
    media_valor = df[coluna].mean()
    
    return min_valor, max_valor, media_valor

# Função para converter um arquivo de texto para Parquet
def converter_txt_para_parquet(arquivo_txt):
    # Lendo o arquivo de texto
    df = pd.read_csv(arquivo_txt)  # Altere o delimitador conforme necessário
    
    # Salvando o DataFrame como arquivo Parquet
    df.to_parquet('measurement_convertidos.parquet')

# Exemplo de uso
# Converter um arquivo de texto para Parquet
converter_txt_para_parquet('/home/gabi/Documents/Git/M9-Individual/Ponderada 9/measurements.txt')

# Calcular estatísticas de um arquivo Parquet
min_valor, max_valor, media_valor = calcular_estatisticas_parquet('measurement_convertidos.parquet')
print("Mínimo:", min_valor)
print("Máximo:", max_valor)
print("Média:", media_valor)
