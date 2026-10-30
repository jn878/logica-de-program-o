import os
os.system("cls")
i = 0
lista_nome= []
lista_sobrenome = []

while True:
    print(""" HOSPITAL
        1- cadastrar
        2- exibir pacientes e identificação
        3- alteração de cadastro
        4- excluir


""")
    opcao = int(input("digite uma opção "))

    match opcao:
        case 1:
            print("== CADASTRO == ")
            nome = input("digite seu nome ").strip()
            sobrenome = input("digite seu sobrenome ").strip()

            if nome and sobrenome == "":
                print("o campo não pode estar vazio")
            else:
                lista_nome.append(nome)
                lista_sobrenome.append(sobrenome)
                print("cadastrado com sucesso")


        case 2:
            print(" EXIBIR CADASTROS ")
            if len == 0:
                print("\nNão existe cadastros ativos")
            else:
                for i, nome in enumerate(lista_nome):
                    print(f" nome {len(lista_nome)} cadastro {i+1}")


        case 3:
            print (" ATUALIZAR CADASTROS ")
            atualizacao_nome = input(" insira o nome do paciente do paciente    ")
            atualizacao_sobrenome = input("insira o sobrenome do paciente   ")

            if nome and sobrenome in lista_nome and lista_sobrenome:
                alteracao_nome = lista_nome.index(nome)
                alteracao_sobrenome = lista_sobrenome.index(sobrenome)

                novo_nome = input("digite o novo nome    ")
                novo_sobrenome = input("digite o novo sobrenome ")

                lista_nome[alteracao_nome] = novo
                lista_sobrenome[alteracao_sobrenome] = novo_sobrenome

                print(f"nome e sobrenome alterado com sucesso para {novo_nome} {novo_sobrenome}")


        case 4:
            print(" EXCLUIR ")
            numero = input("insira o cadastro que sera removido")
            #if numero in




