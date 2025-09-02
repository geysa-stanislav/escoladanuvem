# 1. Importar o módulo csv
import csv

# 2. Definir o nome do arquivo que será lido
nome_arquivo = 'informacoes_pessoais.csv'

try:
    # 3. Abrir o arquivo em modo de leitura ('r')
    # O 'with' garante que o arquivo será fechado corretamente
    # 'encoding="utf-8"' é importante para ler acentos corretamente
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
        # Criar um objeto "leitor" que interpreta o CSV
        # Usamos DictReader para que cada linha seja lida como um dicionário,
        # o que facilita o acesso aos dados pelo nome da coluna.
        leitor_csv = csv.DictReader(arquivo_csv)

        print(f"--- Conteúdo do arquivo '{nome_arquivo}' ---")

        # 4. Iterar sobre cada linha do arquivo
        for linha in leitor_csv:
            # A variável 'linha' é um dicionário para cada registro.
            # Ex: {'Nome': 'Ana Silva', 'Idade': '28', 'Cidade': 'São Paulo'}
            # Acessamos os valores usando as chaves (os nomes das colunas).
            print(f"Nome: {linha['Nome']}, Idade: {linha['Idade']}, Cidade: {linha['Cidade']}")

except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado!")
    print("Por favor, certifique-se de que o arquivo existe na mesma pasta que o script.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")