import os
os.system("cls")


#Função com parametros e com retorno.
def calcular_notas(nota1, nota2):
    resultado = (nota1 + nota2) / 2
    return resultado



print("solicitando dados")
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a primeira nota: "))

#Usando a função com parametros e inserindo o retorno na varieavel soma
media = calcular_notas(nota1, nota2)

print("Exibindo notas")
print(f"media: {media}")