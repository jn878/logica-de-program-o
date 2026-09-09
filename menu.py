
print('''picanha
codigo  |     nome             |   valor
1 -     |  picanha             |   25,00 $
2-      |  lasanha             |   20,00 $
3-      |  strogonoff          |   18,00 $
4-      |  bife acebolado      |   15,00 $
5-      |  pao com ovo         |   5,00  $
''')

codigo = int(input("digite o codigo do prato :"))




match codigo:
    case 1:
        print("picanha | valor | 25,00 $")
    case 2:
        print("lasanha | valor | 20,00 $")
    case 3:
        print("strogonoff | valor | 18,00 $")
    case 4:
        print("bife acebolado | 15,00 $")
    case 5:
        print("pão com ovo | valor | 5,00 $")
    case _:
        print("este codigo não esta disponivel")