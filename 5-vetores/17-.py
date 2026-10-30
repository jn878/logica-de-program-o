import os
os.system("cls")


lista_produtos = []

while True:
    os.system("cls")
    print(""" MERCADINHO SENAI
            1- Cadastrar produto
            2- Listar todos os produtos
            3- Atualizar produto
            4- Remover produto
            5- Buscar produto
            0- Sair
    """)

    opcao = int(input("escolha uma opção "))


    match opcao:
        case 1:
            #CREATE (INSERIR)
            print("CADASTRAR PRODUTOS")
            cadastro = input("\ninsira o nome do produto ").strip().lower()
            if cadastro == "":
                print("o campo não pode estar vazio")
            elif cadastro in lista_produtos:
                print("o produto ja esta cadastrado")
            else:
                lista_produtos.append(cadastro)
                print("produto cadastrado com sucesso")



        case 2:
            # READ (LER/BUSCAR)
            print("== LISTAR TODOS PRODUTOS ==")
            if len == 0:
                print("estoque esta vazio")
            else:
                for i, cadastro in enumerate(lista_produtos):
                    print(f" produtos disponiveis no estoque {len(lista_produtos)}")


        case 3:
            # UPDATE (ATUALIZAR)
            print("== ATUALIZAR PRODUTO ==")
            nome = input("Qual produto deseja atualizar ")
            if nome in lista_produtos:
                posicao = lista_produtos.index(nome)
                novo = input(" novo nome: ")
                lista_produtos[posicao] = novo
                print("Produto alterado com sucesso")
            else:
                print("produto não encontrado")

        case 4:
            # DELETE (REMOVER/DELETAR)
            print("REMOVER PRODUTO")

            nome = input("Qual produto deseja remover ")
            if nome in lista_produtos:
                lista_produtos.remove(nome)
                print("Produto removido com sucesso")
            else:
                print("produto não encontrado")

        case 5:
            #READ (LER / CONSULTAR / BUSCAR)
            print("== BUSCAR PRODUTO ==")
            busca = input("digite o nome do produto que deseja buscar ")
            if busca in lista_produtos:
                print("o produto esta no estoque ")
            else:
                print("produto não esta no estoque")

        case 0:
            print("sistema encerrado")
            break

        case _:
            print("algo deu errado !    \ntente novamente ")

    input("pressione enter para continuar")