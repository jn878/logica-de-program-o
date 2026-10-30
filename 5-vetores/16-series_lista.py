import os

series_lista = []

while True:
    
    print(""" Prime Video
        1- cadastrar serie
        2- pesquisar serie
        0-sair do aplicativo
        """)
    
    opcao = ("escolha um opção")
    
    match serie:
        case 1:
            nome = input("nome da serie que sera cadastrada").strip().upper()
            if nome == "":
                print("o campo não pode estar vazio")
            elif nome in series_lista:
                print("esta serie ja esta disponivel no aplicativo !")
            else:
                series_lista.append(nome)
                print("serie cadastrada com sucesso !")
                
        case 2:
            serie = input("digite um nome de uma serie")
            if len == series_lista:
                print(f"esta serie esta disponivel {len(serie)}")
                print("pressione enter para sair")
                input("pressione enter para continuar")
                os.system("cls")

                
        case 0:
            print("o programa foi encerrado")
            break
        case _:
            print("algo deu errado")
            
            
