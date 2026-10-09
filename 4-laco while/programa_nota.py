import os
os.system("cls")
nota = 0.0
nota_inserida = 0.0


while True:
        for i in range(2):
                nota = float(input(f"digite a nota {i+1} "))
                resposta = input("deseja inserir mais uma nota ? ")
                media = nota * 2 / 3
        match resposta:
                case "nao":
                        print(f"\nmedia {media}")
                        input("aperte enter pra limpar o terminal")
                        os.system("cls")
                case "sim":
                        nota_inserida =  float(input("digite mais uma nota! "))
                        media_nova = i + i + nota_inserida / 3
                        print(f"\nmedia {media_nova} ")
                        os.system("cls")
                        break
                case _:
                        print("*algo deu errado tente novamente*!")