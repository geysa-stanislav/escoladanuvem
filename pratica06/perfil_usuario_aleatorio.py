#Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'.
# O programa deve exibir o nome, email e país do usuário gerado.
import requests

def gerar_perfil_aleatorio():
  """
  Gera um perfil de usuário aleatório usando a API Random User Generator.

  Retorna um dicionário com o nome completo, e-mail e país do usuário.
  """
  url = "https://randomuser.me/api/"
  response = requests.get(url)
  data = response.json()
  usuario = data['results'][0]

  nome = f"{usuario['name']['first']} {usuario['name']['last']}"
  email = usuario['email']
  pais = usuario['location']['country']

  return {
      'nome': nome,
      'email': email,
      'pais': pais
  }

# --- Bloco principal ---
if __name__ == "__main__":
  perfil = gerar_perfil_aleatorio()

  print("--- Perfil de Usuário Aleatório ---")
  print(f"Nome: {perfil['nome']}")
  print(f"E-mail: {perfil['email']}")
  print(f"País: {perfil['pais']}")
