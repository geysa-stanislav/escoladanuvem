"""
Crie uma função que verifique se uma palavra ou frase é um palíndromo 

(lê-se igual de trás para frente, ignorando espaços e pontuação).

Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.

"""

import string

def eh_palindromo(frase: str) -> bool:
  
  """
  Verifica se uma frase é um palíndromo, ignorando espaços,
  pontuação e diferenças entre maiúsculas e minúsculas.

  Parâmetros:
    frase (str): A frase a ser verificada.

  Retorna:
    bool: True se for um palíndromo, False caso contrário.

    """
  
  # 1. Pede para o usuário digitar uma palavra ou frase.
frase_usuario = input("Digite uma palavra ou frase: ")

# 2. Limpa a frase:
#    - .lower() converte tudo para minúsculas.
#    - "" é uma string vazia que vamos preencher.
#    - O 'for' percorre cada letra da frase.
#    - .isalnum() verifica se o caractere é uma letra ou número.
frase_limpa = ""
for letra in frase_usuario.lower():
    if letra.isalnum():
        frase_limpa += letra

# 3. Compara a string limpa com ela mesma invertida.
#    A mágica `[::-1]` inverte qualquer string no Python.
if frase_limpa == frase_limpa[::-1]:
    print("Sim")
else:
    print("Não")