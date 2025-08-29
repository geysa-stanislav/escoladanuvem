"""

2- Classificador de Idade


Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

Criança (0-12 anos),

Adolescente (13-17 anos),

Adulto (18-59 anos)

Idoso (60 anos ou mais)

"""

# Solicita a idade ao usuário e converte a entrada para um número válido
idade = int(input("Digite a sua idade:  "))

# Verifica se a idade é um número negativo (inválido)
if idade < 0:
    print("Por favor, digite uma idade válida (número maior ou igual a zero).")
# Classifica como criança
elif idade <= 12:
    print("Classificação: CRIANÇA")
# Classifica como adolescente
elif idade <= 17:
    print("Classificação: ADOLESCENTE")
# Classifica como adulto 
elif idade <= 59:
    print("Classificação: ADULTO")
# Se nenhuma das anteriores for verdadeira, a pessoa é idosa
else:    
    print("Classificaçaõ:  IDOSO")
    