"""

 Conversor de Temperatura 

Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 

O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

"""

# Função para converter Celsius para outras unidades
def converter_de_celsius(valor, unidade_destino):
    if unidade_destino == 'F':
        # Fórmula: (Celsius * 9/5) + 32
        return (valor * 9/5) + 32
    elif unidade_destino == 'K':
        # Fórmula: Celsius + 273.15
        return valor + 273.15

# Função para converter Fahrenheit para outras unidades
def converter_de_fahrenheit(valor, unidade_destino):
    if unidade_destino == 'C':
        # Fórmula: (Fahrenheit - 32) * 5/9
        return (valor - 32) * 5/9
    elif unidade_destino == 'K':
        # Primeiro, converte para Celsius e depois para Kelvin
        celsius = (valor - 32) * 5/9
        return celsius + 273.15

# Função para converter Kelvin para outras unidades
def converter_de_kelvin(valor, unidade_destino):
    if unidade_destino == 'C':
        # Fórmula: Kelvin - 273.15
        return valor - 273.15
    elif unidade_destino == 'F':
        # Primeiro, converte para Celsius e depois para Fahrenheit
        celsius = valor - 273.15
        return (celsius * 9/5) + 32

# --- Início do Programa ---

# 1. Pede ao usuário para inserir a temperatura
temperatura_str = input("Digite a temperatura (ex: 25): ")
# Converte o texto digitado para um número decimal (float)
temperatura = float(temperatura_str)

# 2. Pede a unidade de origem
unidade_origem = input("Qual a unidade de origem? (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper()

# 3. Pede a unidade de destino
unidade_destino = input("Para qual unidade deseja converter? (C, F, K): ").upper()

# Variável para guardar o resultado
resultado = 0

# 4. Verifica as unidades e chama a função correta
if unidade_origem == 'C':
    resultado = converter_de_celsius(temperatura, unidade_destino)
elif unidade_origem == 'F':
    resultado = converter_de_fahrenheit(temperatura, unidade_destino)
elif unidade_origem == 'K':
    resultado = converter_de_kelvin(temperatura, unidade_destino)
else:
    print("Unidade de origem inválida!")

# 5. Mostra o resultado final formatado com duas casas decimais
# O :.2f dentro do f-string formata o número
print(f"O resultado da conversão é: {resultado:.2f} {unidade_destino}")