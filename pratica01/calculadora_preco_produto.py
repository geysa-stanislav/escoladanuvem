# 1. Pede ao usuário para digitar as informações da compra
# Para o nome, não precisamos de conversão, pois input() já retorna texto.
nome_produto = input("Digite o nome do produto: ")

# Para o preço, convertemos para float() para aceitar casas decimais.
preco_unitario = float(input("Digite o preço unitário (ex: 12.40): "))

# Para a quantidade, convertemos para int() pois é um número inteiro.
quantidade = int(input("Digite a quantidade: "))


# 2. Calcula o preço total (a lógica não muda)
preco_total = preco_unitario * quantidade


# 3. Exibe o resumo organizado da compra (a lógica não muda)
print("\n--- Resumo da Compra ---")
print(f"Produto: {nome_produto}")
print(f"Preço Unitário: R$ {preco_unitario:.2f}")
print(f"Quantidade: {quantidade}")
print("------------------------")
print(f"Valor Total: R$ {preco_total:.2f}")