""""
Desenvolva um programa que calcula o consumo médio de combustível de um veículo.
Use os seguintes dados:

Distância percorrida: 300 km
Combustível gasto: 25 litros 

O programa deve calcular o consumo médio (km/l) 
e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.

"""
# Dados da viagem
distancia_percorrida = 300 # quilômetros (km)
combustivel_gasto = 25 # litros (l)

# Cálculo do consumo
consumo = distancia_percorrida / combustivel_gasto # 300 / 25

# Exibição dos resultados
print("--- Relatório da Viagem ---")
print(f"Distância Percorrida: {distancia_percorrida} km")
print(f"Combustível Gasto: {combustivel_gasto} litros")
print(f"Consumo Médio: {consumo:.2f} km/l")