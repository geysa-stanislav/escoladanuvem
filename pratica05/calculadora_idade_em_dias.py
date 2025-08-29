#Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.

from datetime import date

def calcular_idade_em_dias(ano_nascimento: int) -> int:
  """
  Calcula a idade de uma pessoa em dias, considerando os anos bissextos.

  A contagem é feita a partir do primeiro dia do ano de nascimento até a data atual.

  Parâmetros:
    ano_nascimento (int): O ano em que a pessoa nasceu.

  Retorna:
    int: O número total de dias vividos.
  """
  hoje = date.today()

  # Validação para não aceitar um ano futuro
  if ano_nascimento > hoje.year:
    raise ValueError("O ano de nascimento não pode ser no futuro.")

  # Cria um objeto de data para 1º de janeiro do ano de nascimento
  data_nascimento = date(ano_nascimento, 1, 1)

  # Calcula a diferença entre a data de hoje e a data de nascimento
  diferenca = hoje - data_nascimento

  # Retorna o número de dias dessa diferença
  return diferenca.days

# --- Programa Interativo ---
try:
  # Pede ao usuário o ano de nascimento e converte para inteiro
  ano = int(input("Digite seu ano de nascimento: "))

  # Chama a função para obter o resultado
  dias_vividos = calcular_idade_em_dias(ano)

  # Exibe o resultado para o usuário
  print(f"\nVocê viveu aproximadamente {dias_vividos} dias até hoje.")

except ValueError as e:
  # Mostra um erro se o ano for inválido (futuro ou não numérico)
  print(f"\nErro: {e}. Por favor, insira um ano válido.")
except TypeError:
  # Mostra um erro se o usuário digitar um texto
  print("\nErro: Por favor, digite o ano apenas com números.")