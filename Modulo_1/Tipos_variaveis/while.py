#Loop para repetir enquanto a condição for verdadeira

print("Exemplo de While:")
contador = 0 
while contador < 5:
    print("Contagem", contador)
    contador += 1
    if contador == 5:
        break
print("Programa finalizado com Break!")