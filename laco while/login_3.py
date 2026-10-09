

LOGIN_CORRETO = "admin"
SENHA_CORRETA = "1234"

tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    login = input("Introduza o seu login: ")
    senha = input("Introduza a sua senha: ")
    
    tentativas += 1
    
    if login == LOGIN_CORRETO and senha == SENHA_CORRETA:
        print("\nLogin efetuado com sucesso! Bem-vindo.")
        break
    else:
        tentativas_restantes = max_tentativas - tentativas
        if tentativas_restantes > 0:
            print(f"Login ou senha incorretos. Restam {tentativas_restantes} tentativa(s).\n")
        else:
            print("\nNumero máximo de tentativas ultrapassado. Programa finalizado.")
