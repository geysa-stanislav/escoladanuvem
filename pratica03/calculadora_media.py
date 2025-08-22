"""

Calculadora da Média


Faça um programa que leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno.
 Calcule a média com pesos 2, 3, 4 e 1, respectivamente, 
 para cada uma destas notas e mostre esta média acompanhada pela mensagem "Media: ". 

Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.".
 Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.".
   Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, 
   o programa deve imprimir a mensagem "Aluno em exame.".

 No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno.
   Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada.
     Recalcule a média (some a pontuação do exame com a média anteriormente calculada e divida por 2).
       e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais) ou "Aluno reprovado.", 
       (caso a média tenha ficado 4.9 ou menos). 

Para estes dois casos
(aprovado ou reprovado após ter pego exame) apresente na última linha uma mensagem "Media
final: " seguido da média final para esse aluno.


Entrada: A entrada contém quatro números de ponto flutuante correspondentes às notas dos alunos.


Saída: Todas as respostas devem ser apresentadas com uma casa decimal.
 As mensagens devem ser impressas conforme a descrição do problema.

 """

# --- 1. Entrada das Notas ---

# O problema geralmente espera que as 4 notas venham em uma única linha, separadas por espaço.
# A linha abaixo lê essa linha, divide os valores pelos espaços e os converte para números decimais.
# Se preferir ler uma nota por vez, use 4x a linha: nota1 = float(input())
try:
    n1, n2, n3, n4 = map(float, input("Digite as 4 notas separadas por espaço: ").split())
except ValueError:
    print("Entrada inválida. Por favor, digite quatro números.")
    exit()

# --- 2. Cálculo da Média Ponderada ---

# Pesos definidos no problema: 2, 3, 4 e 1. A soma dos pesos é 10.
peso1, peso2, peso3, peso4 = 2, 3, 4, 1
soma_pesos = peso1 + peso2 + peso3 + peso4

# Fórmula da média ponderada: (nota1*peso1 + nota2*peso2 + ...) / (soma dos pesos)
media = (n1 * peso1 + n2 * peso2 + n3 * peso3 + n4 * peso4) / soma_pesos

# Imprime a média inicial, formatada com uma casa decimal.
# O :.1f garante a formatação correta.
print(f"Media: {media:.1f}")

# --- 3. Verificação da Situação do Aluno ---

# Se a média for 7.0 ou superior
if media >= 7.0:
    print("Aluno aprovado.")

# Se a média for inferior a 5.0
elif media < 5.0:
    print("Aluno reprovado.")

# Se a média estiver entre 5.0 e 6.9 (o 'else' cobre este caso,
# pois as condições anteriores não foram atendidas)
else:
    print("Aluno em exame.")

    # --- 4. Lógica para o Aluno em Exame ---

    # Pede a nota do exame e a converte para número decimal
    nota_exame = float(input("Digite a nota do exame: "))

    # Mostra a nota do exame que foi digitada
    print(f"Nota do exame: {nota_exame:.1f}")

    # Recalcula a média final, conforme a regra do problema
    media_final = (media + nota_exame) / 2

    # Verifica a nova condição para aprovação
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    # Mostra a média final, formatada com uma casa decimal
    print(f"Media final: {media_final:.1f}")