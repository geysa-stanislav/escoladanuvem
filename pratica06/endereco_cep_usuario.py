"""

Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário,
 utilizando a API ViaCEP. 
O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.

"""
import requests

def buscar_cep(cep):
  """
  Busca informações de endereço a partir de um CEP na API ViaCEP.

  Args:
    cep: Uma string contendo o CEP a ser consultado.

  Returns:
    Um dicionário com os dados do endereço ou None se a busca falhar.
  """
  url = f"https://viacep.com.br/ws/{cep}/json/"
  try:
    response = requests.get(url)
    response.raise_for_status()  # Lança um erro para status de resposta ruins (4xx ou 5xx)
    dados = response.json()
    
    if 'erro' in dados:
      print("CEP não encontrado.")
      return None
    else:
      return dados
      
  except requests.exceptions.RequestException as e:
    print(f"Ocorreu um erro na requisição: {e}")
    return None

def exibir_endereco(endereco):
  """Exibe as informações do endereço formatadas."""
  print("\n--- Informações do Endereço ---")
  print(f"Logradouro: {endereco.get('logradouro', 'Não disponível')}")
  print(f"Bairro: {endereco.get('bairro', 'Não disponível')}")
  print(f"Cidade: {endereco.get('localidade', 'Não disponível')}")
  print(f"Estado: {endereco.get('uf', 'Não disponível')}")

# --- Bloco principal de execução ---
if __name__ == "__main__":
  cep_input = input("Digite o CEP (apenas números): ")
  
  if len(cep_input) == 8 and cep_input.isdigit():
    dados_endereco = buscar_cep(cep_input)
    if dados_endereco:
      exibir_endereco(dados_endereco)
  else:
    print("Formato de CEP inválido. Digite 8 números.")