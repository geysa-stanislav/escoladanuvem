# 1. Pede ao usuário para digitar o primeiro númer e esperar por uma resposta
# A função input() pega o que o usuário digitou como TEXTO
# A função int() trasnforma esse texto em um NÚMERO INTEIRO.
numero1 = int(input("Digite o primeiro número:"))

# 2. Pede ao usuário pelo segundo número
numero2 = int(input("Digite o segundo número: "))

# 3. Calcula a soma dos dois números e guarda o resultado em uma nova variável
soma = numero1 + numero2

# 4. Exibe o resultado final na tela de uma forma amigável 
print(f"O resultado da soma de {numero1} + {numero2} é: {soma}")
