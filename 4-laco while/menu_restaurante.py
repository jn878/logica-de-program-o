import os
os.system("CLS")
cardapio = {
    1: {"prato": "Picanha", "valor": 25.00},
    2: {"prato": "Lasanha", "valor": 20.00},
    3: {"prato": "Strogonoff", "valor": 18.00},
    4: {"prato": "Bife Acebolado", "valor": 15.00},
    5: {"prato": "Pão com ovo", "valor": 5.00}
}

total = 0.0
continuar = "s"

while continuar.lower() == "s":
    print("\n--- CARDÁPIO ---")
    print("Código | Prato | Valor")
    print("---------------------------------")
    for codigo, item in cardapio.items():
        print(f" {codigo} | {item['prato']:<15} | R$ {item['valor']}")
    print("---------------------------------")
    
    # Solicita o código do prato[span_3](start_span)[span_3](end_span)
    opcao = input("\nDigite o código do prato desejado: ")
    
    if opcao.isdigit() and int(opcao) in cardapio:
        prato_escolhido = cardapio[int(opcao)]
        total += prato_escolhido["valor"]
        print(f"-> {prato_escolhido['prato']} adicionado ao pedido.")
    else:
        print("Código inválido! Por favor, escolha uma opção do menu.")
        continue
    
    continuar = input("\nDeseja escolher outro prato? (s/n): ")

print(f"\nTotal a pagar: R$ {total}")
