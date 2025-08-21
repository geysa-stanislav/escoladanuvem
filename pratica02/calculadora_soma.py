# 1- Conversor de Moeda

# Dados fornecidos
valor_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

# Calcula a conversão para dólar e euro
valor_dolares = valor_reais / taxa_dolar
valor_euros = valor_reais / taxa_euro

# Exibe os resultados formatados com duas casas decimais
print(f"Valor em reais: R$ {valor_reais:.2f}")
print("-" * 30)
print(f"Valor em dólares: US$ {valor_dolares:.2f}")
print(f"Valor em euros: € {valor_euros:.2f}")