# Lista -> Coleção ordenada e mutável (pode ser alterada).
# Índices: Começam em 0.


minha_lista = [1, 2, 3, 4, "Teste", True, False]
print("Lista de exemplo", minha_lista)


#Exibindo elementos da lista:
minha_lista[0] = "Python"

print("Lista na posição 0:", minha_lista[0])
print("Lista na posição 5", minha_lista[4])  # Quinto elemento → 5
print("Lista do elemento indice 1 ao 4:", minha_lista[1:5])
print("Lista de elementos indice 0 ao 4", minha_lista[:5]) #Fatiamento de listas (slicing)  - O valor do "fim" funciona como parada, não como parte da seleção.
print("Lista de elementos indice 2 ao final", minha_lista[2:])
print("\n")

print("Utilização de métodos -> append() / index() / insert(posicao, valor) / pop(indice)")
# Método Append -> Adiciona um item no final da lista
minha_lista.append(6)
print("Método APPEND: ", minha_lista)

# Método INDEX -> Remove e retorna um elemento pelo índice.
indice = minha_lista.index(6)
print("Método Index: ", indice)  # Exibe o índice do número 6 na lista

# Método INSERT -> Insere um item em um índice específico.
minha_lista.insert(2, 10)  
print("Método Insert: ",minha_lista)

# Método POP(indice) → Remove e retorna um elemento pelo índice.
elemento_removido = minha_lista.pop(3)  
print("Método Pop - Removendo elemento",elemento_removido)  # Remove o valor do índice 3(3)
print(minha_lista)        # Lista sem esse item

# Método REMOVE(valor) Remove o primeiro elemento que tenha o valor informado.
minha_lista.remove("Python")  
print("Método Remove - Removendo o VALOR informado (Python)",minha_lista)


#Método para organização de lista sort()

lista_ordenada = [5, 6, 3, 15, 8, 10]
lista_ordenada.sort()
print("Método SORT() - Imprime lista ordenada.", lista_ordenada)
