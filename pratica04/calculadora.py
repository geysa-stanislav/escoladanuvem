"""

Desenvolva uma calculadora em Python que realize as quatro operações básicas 
(adição, subtração, multiplicação e divisão) entre dois números.
 A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. Siga as especificações abaixo:



A calculadora deve solicitar ao usuário que insira dois números e uma operação.

As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).

O programa deve continuar solicitando entradas até que uma operação válida seja concluída.

Trate os seguintes erros:

Entrada inválida (não numérica) para os números

Divisão por zero

Operação inválida



Use try/except para capturar e tratar os erros apropriadamente.

Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.

Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa.

"""

def calculadora():
    """
    Calculadora que realiza as quatro operações básicas e trata erros de entrada.
    """
    while True:
        try:
            # 1. Solicita e converte os números de entrada
            num1_str = input("Digite o primeiro número: ")
            num1 = float(num1_str)
            
            num2_str = input("Digite o segundo número: ")
            num2 = float(num2_str)

            # 2. Solicita a operação
            operacao = input("Digite a operação (+, -, *, /): ")

            # 3. Realiza o cálculo baseado na operação
            resultado = 0
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                # 3a. Trata especificamente a divisão por zero antes de calcular
                if num2 == 0:
                    raise ZeroDivisionError("Erro: Não é possível dividir por zero.")
                resultado = num1 / num2
            else:
                # 3b. Lança um erro se a operação for inválida
                raise ValueError("Erro: Operação inválida. Por favor, use '+', '-', '*' ou '/'.")
            
            # 4. Se tudo deu certo, exibe o resultado e encerra o loop
            print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")
            break

        except ValueError as e:
            # Captura erro de conversão de número ou operação inválida
            print(f"\nEntrada inválida: {e}")
            print("Por favor, tente novamente.\n")
            continue
            
        except ZeroDivisionError as e:
            # Captura a tentativa de divisão por zero
            print(f"\nErro de operação: {e}")
            print("Por favor, tente novamente.\n")
            continue

        except Exception as e:
            # Captura qualquer outro erro inesperado
            print(f"\nOcorreu um erro inesperado: {e}")
            print("Por favor, tente novamente.\n")
            continue

# Executa a função da calculadora
calculadora()
