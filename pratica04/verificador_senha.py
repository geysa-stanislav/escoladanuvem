"""

Crie um programa que verifique se uma senha é forte.

 Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. 

 O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.

 """

def verificar_forca_senha():
    """
    Este programa verifica se uma senha é forte.
    - Requisitos: Mínimo de 8 caracteres e pelo menos um número.
    - Continua pedindo uma senha até que uma válida seja inserida
      ou o usuário digite 'sair'.
    """
    print("--- Verificador de Senha Forte ---")
    print("Uma senha forte deve ter:")
    print("  1. Pelo menos 8 caracteres de comprimento.")
    print("  2. Pelo menos um número (0-9).")
    print("-" * 35)

    while True:
        senha = input("Digite uma senha (ou 'sair' para encerrar): ")

        # 1. Verifica se o usuário quer sair
        if senha.lower() == 'sair':
            print("Programa encerrado.")
            break

        # 2. Inicializa as variáveis de verificação
        comprimento_ok = False
        tem_numero = False

        # 3. Verifica o comprimento da senha
        if len(senha) >= 8:
            comprimento_ok = True

        # 4. Verifica se a senha contém pelo menos um número
        for caractere in senha:
            if caractere.isdigit():
                tem_numero = True
                break  # Encontrou um número, não precisa continuar procurando

        # 5. Avalia os critérios e dá o feedback
        if comprimento_ok and tem_numero:
            print("\n✅ Senha forte e válida! Senha aceita.")
            break  # Encerra o programa com sucesso
        else:
            print("\n❌ Senha fraca. Por favor, tente novamente.")
            if not comprimento_ok:
                print(f"   - Faltam {8 - len(senha)} caracteres (mínimo de 8).")
            if not tem_numero:
                print("   - Sua senha precisa conter pelo menos um número.")
            print("-" * 35)


# Executa a função principal
verificar_forca_senha()