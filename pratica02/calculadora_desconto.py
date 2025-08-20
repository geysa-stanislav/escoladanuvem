# 2- Calculadora de Desconto

# Informações do produto
nome_produto = "Camiseta"
preco_original = 50.00
percentual_desconto = 20

# 1. Calcula o valor do desconto
#    Fórmula: (preço * percentual) / 100
valor_do_desconto = (preco_original * percentual_desconto) / 100

# 2. Calcula o preço final com o desconto aplicado
#    Fórmula: preço original - valor do desconto
preco_final = preco_original - valor_do_desconto

# 3. Exibe todos os detalhes de forma organizada
print("-" * 30)
print("      Calculadora de Desconto")
print("-" * 30)
print(f"Produto: {nome_produto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Desconto: {percentual_desconto}%")
print("-" * 30)
print(f"Valor do Desconto: R$ {valor_do_desconto:.2f}")
print(f"Preço Final: R$ {preco_final:.2f}")
print("-" * 30)