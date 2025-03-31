# Lista -> Coleção de elementos ordenados e mutaveis (variável pode ser modificada).
#Indice inicia-se do 0 até o total


minha_lista = [1, 2, 3, 4, 5, "Lucas", True, False]
lista_ordenada = [5, 6, 3, 15, 8, 10]

print("Minha lista de exemplo: ", minha_lista)

print("\n")
#Exibição de elementos:

minha_lista[0] = "Python"
print("Primeiro elemento adicionado 'python' -> Linha 27 [0]: ", minha_lista[0])
print("Quarto elemento: [4]", minha_lista[4])

#Pratica de fatiar uma lista, sempre traz um elemento a menos que o último selecionado!

print("Trazendo somente parte fateada da lista: ",minha_lista[2:5])
print("Trazendo do inicio a parte fateada da lista: ",minha_lista[:5])
print("Trazendo do elemento selecionado ao final: ",minha_lista[2:])

print("\n")
# Lista mutável 
"""
Método append(): Adiciona elemento no final da lista 
"""
minha_lista.append(6)
print("Lista utilizando método APPEND():", minha_lista)

print("\n")
#Método Index -> retorna a posição do elemento na lista, contado a partir da posição 0

indice = minha_lista.index(6)
print("Indice do elemento 6:", indice )

print("\n")
#Método de inserir elemento em indice 

minha_lista.insert(2, 10)
print("Lista após acrescentar o número 10 na posição 2 da lista",minha_lista)

print("\n")
#Método POP() -> Remove o elemento selecionado no indice

elemento_removido = minha_lista.pop(3)
print("Elemento removido: ", elemento_removido)
print("Lista após execução do Método POP(0): ", minha_lista)

print("\n")
#Método Remove -> Utilizado para remover elemento selecionado no parâmetro

minha_lista.remove("Python")
print("Lista após utilizar método REMOVE('Python'):",minha_lista)


#Método para organizar lista em ordem crescente

lista_ordenada.sort()
print("Lista após organizar elementos em ordem crescente:", lista_ordenada)