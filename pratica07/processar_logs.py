# Importa a biblioteca pandas, que é excelente para manipulação de dados
import pandas as pd

# Define o nome do arquivo que queremos ler
nome_arquivo = 'logs.csv'

try:
    # Usa o pandas para ler o arquivo CSV e carregá-lo em uma tabela (DataFrame)
    dados = pd.read_csv(nome_arquivo)

    # Seleciona apenas a coluna 'tempo_execucao' da tabela
    tempos = dados['tempo_execucao']

    # Calcula a média dos valores da coluna
    media = tempos.mean()

    # Calcula o desvio padrão dos valores da coluna
    # O 'ddof=0' é para calcular o desvio padrão populacional, se quiser o amostral, remova-o.
    desvio_padrao = tempos.std()

    # Imprime os resultados formatados na tela
    print("--- Análise de Logs de Treinamento ---")
    print(f"Média do tempo de execução: {media:.2f}")
    print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f}")

except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado!")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")