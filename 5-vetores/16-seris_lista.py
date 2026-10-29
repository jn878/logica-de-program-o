import os

series_lista = []

while True:
    
    print(""" Prime Video
        1- cadastrar serie
        2- pesquisar serie
        3- ver series disponiveis
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
                print(f"esta serie esta disponivel {serie}")
                print("pressione enter para sair")
                
                
                
            
            
