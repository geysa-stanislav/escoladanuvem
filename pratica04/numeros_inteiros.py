"""

Crie um programa que solicite ao usuário que insira números inteiros.

 O programa deve continuar solicitando números até que o usuário digite 'fim'.
  
 Para cada número inserido, o programa deve informar se é par ou ímpar. 
 
 Se o usuário inserir algo que não seja um número inteiro, o programa deve

informar o erro e continuar. No final, o programa deve exibir a quantidade de números pares e ímpares inseridos.

"""
        

def classificar_numeros():
    """
    Este programa solicita números inteiros, classifica cada um como par ou ímpar,
    e no final exibe a contagem total de cada tipo.
    - Ignora entradas que não são números inteiros.
    - Encerra quando o usuário digita 'fim'.
    """
    # 1. Inicializa os contadores
    pares = 0
    impares = 0

    print("--- Classificador de Números Pares e Ímpares ---")
    print("Digite números inteiros um por um.")
    print("Qualquer entrada não-inteira será ignorada.")
    print("Digite 'fim' para encerrar e ver o resultado.")
    print("-" * 50)

    while True:
        entrada = input("Digite um número inteiro ou 'fim': ")

        # 2. Verifica se o usuário quer sair
        if entrada.lower() == 'fim':
            break

        # 3. Tenta converter a entrada para um inteiro
        try:
            numero = int(entrada)
        except ValueError:
            # Se a conversão falhar (ex: texto ou float), informa o erro e continua
            print(f"Erro: '{entrada}' não é um número inteiro válido. Tente novamente.")
            continue

        # 4. Verifica se o número é par ou ímpar e atualiza o contador
        if numero % 2 == 0:
            print(f"-> {numero} é PAR.")
            pares += 1
        else:
            print(f"-> {numero} é ÍMPAR.")
            impares += 1

    # 5. Ao final do loop, exibe o resumo
    print("-" * 50)
    print("Programa finalizado.")
    print("\n--- Resumo ---")
    print(f"Quantidade de números pares inseridos: {pares}")
    print(f"Quantidade de números ímpares inseridos: {impares}")
    print("-" * 50)

# Executa a função principal do programa
classificar_numeros()