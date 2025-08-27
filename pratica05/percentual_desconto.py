"""
Crie um programa que receba o preço original de um produto e um percentual de desconto,

 realizando o cálculo do preço final após a aplicação do desconto. Requisitos:

Permitir que o usuário informe o preço do produto e o percentual de desconto.

Utilizar operações matemáticas para calcular o valor do desconto e o preço final.

Exibir o preço final com duas casas decimais para garantir precisão. 

Entrada esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10).

"""

try:
    # 1. Pede ao usuário o preço original e o percentual de desconto
    preco_original = float(input("Digite o preço original do produto: R$ "))
    percentual_desconto = float(input("Digite o percentual de desconto (ex: 10 para 10%): "))

    # Validação para garantir que os números não sejam negativos
    if preco_original < 0 or percentual_desconto < 0:
        print("\nErro: Os valores não podem ser negativos.")
    else:
        # 2. Calcula o valor do desconto
        valor_desconto = (preco_original * percentual_desconto) / 100

        # 3. Calcula o preço final subtraindo o desconto
        preco_final = preco_original - valor_desconto

        # 4. Exibe os resultados para o usuário
        print("\n--- Calculando Desconto ---")
        print(f"Preço Original: R$ {preco_original:.2f}")
        print(f"Valor do Desconto ({percentual_desconto}%): R$ {valor_desconto:.2f}")
        print(f"Preço Final: R$ {preco_final:.2f}")

except ValueError:
    # Captura o erro se o usuário digitar um texto em vez de número
    print("\nErro: Por favor, digite apenas valores numéricos válidos.")