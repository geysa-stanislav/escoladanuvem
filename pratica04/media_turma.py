"""

Crie um programa que permita a um professor registrar as tas de uma turma. 

O programa deve continuar solicitando notas até que o professor digite 'fim'.

Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando.

No final, deve exibir a média da turma.

"""

def calcular_media_turma():
    """
    Este programa registra as notas de uma turma e calcula a média.
    - Aceita notas de 0 a 10.
    - Ignora entradas inválidas (textos ou números fora do intervalo).
    - Para de solicitar notas quando o usuário digita 'fim'.
    - Exibe a média final da turma.
    """
    notas = []
    
    print("--- Registro de Notas da Turma ---")
    print("Digite as notas dos alunos (de 0 a 10).")
    print("Quando terminar, digite 'fim' para calcular a média.")
    print("-" * 35)

    while True:
        entrada = input("Digite uma nota ou 'fim': ")

        # 1. Verifica se o professor quer encerrar o programa
        if entrada.lower() == 'fim':
            break

        # 2. Tenta converter a entrada para um número
        try:
            nota = float(entrada)
        except ValueError:
            # Se a entrada não for um número (ex: "abc"), avisa e ignora
            print("Entrada inválida. Por favor, digite um número ou 'fim'.")
            continue

        # 3. Verifica se a nota está no intervalo válido (0 a 10)
        if 0 <= nota <= 10:
            # Se a nota for válida, adiciona à lista
            notas.append(nota)
        else:
            # Se a nota estiver fora do intervalo, avisa e ignora
            print("Nota inválida. Por favor, insira um valor entre 0 e 10.")

    # 4. Após o loop, calcula e exibe a média
    print("-" * 35)
    if notas:  # Verifica se alguma nota válida foi inserida
        media = sum(notas) / len(notas)
        print(f"Foram registradas {len(notas)} notas válidas.")
        print(f"A média da turma é: {media:.2f}")
    else:
        # Mensagem para o caso de nenhuma nota ter sido digitada
        print("Nenhuma nota válida foi registrada para calcular a média.")
    print("-" * 35)

# Executa a função principal do programa
calcular_media_turma()
