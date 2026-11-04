import os

lista_nome = []
lista_posicao = []
lista_numero = []





while True:
    print(""" 1- cadastrar
            2- listar jogadores
            3- atualizar
            4- excluir

""")
    opcao = int(input(" escolha uma opção"))

    match opcao:
        case 1:
            nome = input("digite seu nome ").strip().lower()
            posicao = input("digite sua posicao")
            numero = int(input("digite o numero da sua camisa"))
