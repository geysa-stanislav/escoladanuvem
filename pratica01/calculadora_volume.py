# 1. Pede ao usuário para digitar as três dimensões da caixa
# Usamos float() para aceitar números com casas decimais (ex: 10.5)
comprimento = float(input("Digite o comprimento da caixa (cm): "))
largura = float(input("Digite a largura da caixa (cm): "))
altura = float(input("Digite a altura da caixa (cm): "))

# 2. Calcula o volume multiplicando as três dimensões fornecidas
volume = comprimento * largura * altura

# 3. Exibe o resultado formatado na tela
# Usamos :.2f para formatar o número para ter apenas 2 casas decimais
print(f"O volume da caixa é de: {volume:.2f} cm³")