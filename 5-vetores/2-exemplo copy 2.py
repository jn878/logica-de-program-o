import os

print("inserir numeros")
vetor_livros = []

for i in range(5):                  # FOR IN RANGE
    livro = (input(f"digite {i+1} livro "))
    vetor_livros.append(livro)


    print(" \nexibindo numeros do vetor ")

for indice, livro in enumerate (vetor_livros, start=1):      # FOR IT
    print(f" {indice} : {livro}")
