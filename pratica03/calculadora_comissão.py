"""

Calculadora de Comissão


Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas
efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão
sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais. 

Entrada: O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de
dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e
montante total das vendas efetuadas por este vendedor, respectivamente. 

Saída: Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.

"""

# 1. Entrada de Dados

# Pede o nome do vendedor e armazena como texto (string).
nome_vendedor = input("Digite o nome do vendedor: ")

# Pede o salário fixo. A função float() converte o texto digitado em um número decimal.
salario_fixo = float(input("Digite o salário fixo: R$ "))

# Pede o total de vendas do mês. Também converte para número decimal.
total_vendas = float(input("Digite o total de vendas no mês: R$ "))


# 2. Cálculos

# Define a taxa de comissão (15% = 15 / 100 = 0.15).
taxa_comissao = 0.15

# Calcula o valor da comissão.
valor_comissao = total_vendas * taxa_comissao

# Soma o salário fixo com o valor da comissão para obter o total a receber.
salario_final = salario_fixo + valor_comissao


# 3. Saída de Dados

# Imprime o resultado final.
# Usamos uma f-string (a letra 'f' antes das aspas) para facilitar a formatação.
# A parte ':.2f' formata a variável 'salario_final' para que ela sempre exiba duas casas decimais.
print(f"TOTAL A RECEBER = R$ {salario_final:.2f}")