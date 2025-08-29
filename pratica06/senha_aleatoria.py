# Crie um programa que gera uma senha aleatória com o módulo random, 
# utilizando caracteres especiais, possibilitando o usuário a informar 
# a quantidade de caracteres dessa senha aleatória.

import random
import string

def gerar_senha_aleatoria(tamanho):
  """
  Gera uma senha aleatória com base no tamanho fornecido.

  A senha inclui letras maiúsculas e minúsculas, dígitos e caracteres especiais.
  
  Args:
    tamanho: O comprimento desejado para a senha.

  Returns:
    A senha aleatória gerada.
  """
  caracteres = string.ascii_letters + string.digits + string.punctuation
  senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
  return senha

if __name__ == "__main__":
  try:
    tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
    
    if tamanho_senha <= 0:
      print("O tamanho da senha deve ser um número positivo.")
    else:
      senha_gerada = gerar_senha_aleatoria(tamanho_senha)
      print(f"Sua senha aleatória é: {senha_gerada}")

  except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")