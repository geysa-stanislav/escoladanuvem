# 1. Importar o módulo csv, que é a ferramenta padrão do Python para trabalhar com CSV
import csv

# 2. Definir o nome do arquivo que será criado
nome_arquivo = 'informacoes_pessoais.csv'

# 3. Definir os cabeçalhos (os nomes das colunas)
cabecalhos = ['Nome', 'Idade', 'Cidade']

# 4. Definir os dados que serão escritos no arquivo
# Cada item da lista é um dicionário, onde a chave é o nome da coluna
dados = [
    {'Nome': 'Ana Silva', 'Idade': 28, 'Cidade': 'São Paulo'},
    {'Nome': 'Bruno Costa', 'Idade': 34, 'Cidade': 'Rio de Janeiro'},
    {'Nome': 'Carla Dias', 'Idade': 45, 'Cidade': 'Belo Horizonte'},
    {'Nome': 'Daniel Farias', 'Idade': 22, 'Cidade': 'Salvador'},
    {'Nome': 'Eduarda Lima', 'Idade': 30, 'Cidade': 'Campo Grande'}
]

# 5. Abrir o arquivo em modo de escrita ('w')
# O 'with' garante que o arquivo será fechado automaticamente no final
# 'newline=""' evita que linhas em branco sejam criadas entre os dados
# 'encoding="utf-8"' garante a compatibilidade com acentos e caracteres especiais
with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    # Criar um objeto "escritor" que sabe como formatar os dados para CSV
    # Usamos DictWriter porque nossos dados são uma lista de dicionários
    escritor = csv.DictWriter(arquivo_csv, fieldnames=cabecalhos)

    # Escrever a primeira linha do arquivo com os cabeçalhos
    escritor.writeheader()

    # Escrever todas as linhas de dados de uma vez
    escritor.writerows(dados)

print(f"Arquivo '{nome_arquivo}' criado com sucesso!")