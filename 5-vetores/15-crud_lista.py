import os
os.system("cls")

lista_produtos = []


while True:
    print(""" MERCADO
    1- cadastrar produto
    2- listar produtos
    0- sair
        
        """)


    opcao = int(input("escolha uma opçao "))


    match opcao:
        case 1:
            print(" cadastrar um produto")
            # strip() retira os espaçõs vazios no final
            # upper() todas as letras maiusculas
            nome = input("nome do novo produto ").strip().upper()
            
            # . append(nome) adiciona o nome do produto na lista
            if nome == "":
                print("preencha o campo.")
            elif nome in lista_produtos:
                print(f"{nome} ja esta cadastrado")
            else:
                lista_produtos.append(nome)
                print("produto cadastrado com sucesso.")
                input("pressione um tecla pra continuar...")
        
        
        case 2:
            if len == 0:
                print("o estoque esta vazio")
            else:
                print(" LISTAGEM DE PRODUTOS ")
                for i,produto in enumerate(lista_produtos):
                    print(f"produtos disponiveis{i+1} = {produto}")
                    print(f"total de produtos: {len(lista_produtos)}")
                    #len(lista_produtos) mostra a quantidade de produtos na lista
            input("\npressione uma tecla pra continuar...")
            
            
        case 0:
            print("sistema finalizado")
            input("pressione uma tecla para continuar ")
            break
        
        
        case _:
            print("algo deu errado")
            print("pressione enter para continuar")
            os.system("cls")