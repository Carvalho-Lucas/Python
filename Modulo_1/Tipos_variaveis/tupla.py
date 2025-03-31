#Coleção ordenada e imutável de uma lista

minha_tupla = ( 1, 2, 2, 3, 4)
print("Minha lista: ", minha_tupla)

print("Print do elemento na posição[1]: ", minha_tupla[1])

#-1 Emite o elemento final da lista

print("\n")
print("Print do elemento na posição[1]: ", minha_tupla[-1])


print("\n")
#Método Count -> para realizar contagem de quantas vezes o elemento é repetido na lista
contagem = minha_tupla.count(2)
print("Quantidade de vezes que o elemento 2 aparece: ", contagem)

print("\n")

#Método Index -> Retorna a posição do elemento pesquisado
indice = minha_tupla.index(2)
print("Indice do elemento 4: ", indice)