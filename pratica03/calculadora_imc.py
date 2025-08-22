"""

Calculadora de IMC


Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.


< 18.5: classificacao = "Abaixo do peso" 

< 25: classificacao = "Peso normal"

 < 30: classificacao = "Sobrepeso"

 Para os demais cenários: classificacao = "Obeso"

 """

# --- Calculadora de IMC ---

# Bloco try-except para garantir que a entrada seja um número válido
try:
    # Solicita o peso do usuário e converte para float (número com decimal)
    peso = float(input("Digite seu peso em kg (ex: 70.5): "))
    
    # Solicita a altura do usuário e converte para float
    altura = float(input("Digite sua altura em metros (ex: 1.75): "))

    # Verifica se os valores inseridos são positivos, pois peso e altura não podem ser zero ou negativos
    if peso <= 0 or altura <= 0:
        print("Erro: O peso e a altura devem ser valores positivos.")
    else:
        # Calcula o IMC: peso dividido pela altura ao quadrado
        imc = peso / (altura ** 2)
        
        # Determina a classificação com base no valor do IMC
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else: # Se nenhuma das condições acima for verdadeira, o IMC é 30 ou maior
            classificacao = "Obeso"
            
        # Exibe o resultado formatado para o usuário
        print("\n--- Resultado ---")
        # O ":.2f" formata o número para ter apenas 2 casas decimais
        print(f"Seu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")

except ValueError:
    # Mensagem de erro se o usuário digitar um texto em vez de um número
    print("Erro: Por favor, digite apenas números para o peso e a altura.")  
    