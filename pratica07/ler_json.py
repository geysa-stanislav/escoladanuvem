"""
Crie um script em Python que leia e escreva dados em um arquivo JSON. 
O arquivo JSON deve conter informações de uma pessoa, com campos nome, idade e cidade.

"""

import json

def ler_json(nome_arquivo):
    """Lê dados de um arquivo JSON e os exibe na tela."""
    try:
        # Adicionado encoding='utf-8' para garantir a leitura correta de acentos
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
            dados = json.load(arquivo_json)
            print("\n--- Lendo dados do arquivo ---")
            print(dados)
            return dados # É uma boa prática retornar os dados lidos
            
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado. Criando um novo.")
        return None # Retorna None se o arquivo não existir

def escrever_json(nome_arquivo, dados):
    """Escreve dados em um arquivo JSON."""
    try:
        # Adicionado encoding='utf-8' para salvar acentos corretamente
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
            # Corrigido: indent precisa de um valor (ex: 4 para formatar)
            json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)
        
        print(f"Dados salvos com sucesso em '{nome_arquivo}'")

    except Exception as e:
  
        print(f"Erro ao salvar os dados: {e}")

# --- Bloco de Execução Principal ---
# A linha abaixo garante que o código só será executado quando o script for rodado diretamente
if __name__ == "__main__":
    
    arquivo = "meus_dados.json"

    
    novos_dados = {
        'nome': 'Mariana Costa',
        'idade': 31,
        'cidade': 'Campo Grande'
    }

    # Chamada das funções
    escrever_json(arquivo, novos_dados)
    ler_json(arquivo)