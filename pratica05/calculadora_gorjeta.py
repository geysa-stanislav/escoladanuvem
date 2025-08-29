"""
Crie uma função que calcule a gorjeta a ser deixada em um restaurante, 

baseada no valor total da conta e na porcentagem de gorjeta desejada. 

Calcule o valor da gorjeta baseado no total da conta e na porcentagem desejada.

Parâmetros: 
valor_conta (float): O valor total da conta

 porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)

Retorna: 

float: O valor da gorjeta calculada

"""
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
  """Calcula a gorjeta com base no valor da conta e na porcentagem."""
  gorjeta = valor_conta * (porcentagem_gorjeta / 100)
  return gorjeta


try:
  # 1. Pede o valor da conta e converte para float (número com decimal)
  valor_conta_usuario = float(input("Digite o valor total da conta: R$ "))

  # 2. Pede a porcentagem e converte para float
  porcentagem_usuario = float(input("Digite a porcentagem da gorjeta que deseja dar (ex: 15): "))

  # 3. Chama a função para fazer o cálculo com os valores do usuário
  gorjeta_calculada = calcular_gorjeta(valor_conta_usuario, porcentagem_usuario)
  total_com_gorjeta = valor_conta_usuario + gorjeta_calculada

  # 4. Mostra o resultado na tela
  print("\n--- Resumo da Conta ---")
  print(f"Gorjeta: R$ {gorjeta_calculada:.2f}")
  print(f"Total a pagar: R$ {total_com_gorjeta:.2f}")

except ValueError:
  # Mensagem de erro se o usuário digitar algo que não seja um número
  print("\nErro: Por favor, digite apenas números válidos.")