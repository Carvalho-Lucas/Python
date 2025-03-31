lista_produtos = ["Arroz", "feijão", "carne", "leite", "ovo", "doce"]

for indice, valor in enumerate(lista_produtos):
    tamanho = len(valor)

    if tamanho > 6:
        lista_produtos[indice] = "GRANDE"
    elif 4 <= tamanho <= 6:
        lista_produtos[indice] = "MÉDIO"
    else:
        lista_produtos[indice] = "PEQUENO"

print(lista_produtos)
   
    # Exibindo o resultado final
"""
    for indice, status in enumerate(lista_produtos):
        print(f"Produto na posição {indice} → {status}")
"""