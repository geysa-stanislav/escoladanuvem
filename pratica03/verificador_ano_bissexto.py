"""
 Verificador de Ano Bissexto


Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.

Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.

"""

# Pede ao usuário para digitar um ano e armazena o valor.
# A função int() converte o texto digitado pelo usuário em um número inteiro.
ano = int(input("Digite um ano para verificar se ele é bissexto: "))

# Agora, vamos verificar as regras do ano bissexto.
# A ordem das verificações é importante.

# Regra 1: O ano é divisível por 4? (O operador '%' retorna o resto de uma divisão)
# Se o resto da divisão por 4 for 0, significa que ele é divisível.
if (ano % 4 == 0):
    # Se o ano é divisível por 4, precisamos checar as exceções (anos centenários).
    # Regra 2: O ano é divisível por 100?
    if (ano % 100 == 0):
        # Se for divisível por 100, ele só será bissexto se também for divisível por 400.
        # Regra 3: O ano é divisível por 400?
        if (ano % 400 == 0):
            # Se passou por todas as regras, é bissexto.
            print(f"O ano {ano} é bissexto.")
        else:
            # É divisível por 100, mas não por 400, então não é bissexto.
            print(f"O ano {ano} NÃO é bissexto.")
    else:
        # É divisível por 4, mas não por 100, então é bissexto.
        print(f"O ano {ano} é bissexto.")
else:
    # Se nem sequer for divisível por 4, então com certeza não é bissexto.
    print(f"O ano {ano} NÃO é bissexto.")