import os
os.system("cls")


qtd_pares = 0
qtd_impares = 0
soma_pares = 0
soma_geral = 0
qtd_total = 0


numero = int(input("Digite um número inteiro positivo (ou 0 para encerrar): "))


while numero != 0:
    if numero > 0:
        
        qtd_total = qtd_total + 1
        soma_geral = soma_geral + numero

        if numero % 2 == 0:
            qtd_pares = qtd_pares + 1
            soma_pares = soma_pares + numero
        else:
            qtd_impares = qtd_impares + 1
    
    
    numero = int(input("Digite um número inteiro positivo (ou 0 para encerrar): "))


print("\n--- RESULTADOS ---")
print(f"Quantidade de pares: {qtd_pares}")
print(f" Quantidade de ímpares: {qtd_impares}")


if qtd_pares > 0:
    media_pares = soma_pares / qtd_pares
    print(f"Média dos valores pares: {media_pares}")
else:
    print(" Média dos valores pares: Nenhum número par foi inserido.")


if qtd_total > 0:
    media_geral = soma_geral / qtd_total
    print(f" Média geral dos números: {media_geral}")
else:
    print(" Média geral dos números: Nenhum número foi inserido.")

