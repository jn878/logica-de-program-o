import os
os.system("cls")

contador = 0
total = 0
total_fml = total + 1




for i in range (1000):
    while True:
        total = input("ola qual seu nome ? ")
        filhos = int(input("quantos filhos voce tem ? "))
        maior_salario = float(input("informe o maior salario da residencia "))
        menor_salario = float(input("informe menor  salario da residencia "))
        
        print(""" 1 |adicionar familia|
        2 |sair e exibir resultados|""")
        
        #variaveis
        salarios_media = maior_salario * menor_salario / 3
        media_filhos = filhos * filhos / 3
        maior_salarios = maior_salario * 2 / 3
        menor_salario = menor_salario * 2 / 3
        contador = 0
        total = 0
        total_fml = total + 1

        painel = int(input("qual das opções "))

        match painel:
            case 1:
                            total = input("ola qual seu nome ? ")
                            salarios = float(input("digite sua media salarial "))
                            filhos = (input("quantos filhos voce tem ? "))
                            maior_salario = (input("informe o maior salario da residencia "))
                            menor_salario = input("informe menor  salario da residencia ")
            case 2:
                    print(f"total de familias que responderam a pesquisa = {total_fml}")
                    print(f"medial salaria da populção {salarios_media}")
                    print(f"media de numeros de filhos {media_filhos }")
                    print(f"maior salario {maior_salario} ")
                    print(f"menor salario "{menor_salario})
        break


salarios_media = maior_salario * menor_salario / 3
media_filhos = filhos * filhos / 3
maior_salarios = contador + 1
menor_salario = contador + 1

