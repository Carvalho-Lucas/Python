#Repitição de código enquanto condição for verdadeira
#Iteração sobre sequência de elementos (Lsita, tupla, dicionário)

lista = [1, 2, 3, 4, 5]

for elemento in lista:
    print("Utilização de lista em for",elemento)

print("\n")

tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    print("Utilização de tupla em for",elemento)

print("\n")

#For -> Dicionário 
pessoa = {"nome": "Lucas", "idade": 27, "cidade": "MG"}
print("For utilizando dicionário - Chave")

#Impressão de chaves
for chave in pessoa.keys():
    print(chave)

#Impressão de valores
print("For utilizando dicionário - Valor")
for valor in pessoa.values():
    print(valor)

#Impressão de chaves/valores
for chave, valor in pessoa.items():
    print(f" Chave: {chave} , Valor: {valor}")

print("\nUtilização função RANGE()")
# Função range() -> retorna um intervalo numérico em formato de lista -> print(list(range(0,10)))

for numero in range(0,5):
    print("Numero", numero)

print("\nUtilização função RANGE() com LEN()")

lista = [1, 2, 3, 4, 5]
for indice in range(0, len(lista)):
    print("Indice", indice)
    print("Elemento", lista[indice])

print("\nUtilização função ENUMERATE()")

lista_enumerate = ["a","b","c","d"]
for indice, valor in enumerate(lista_enumerate):
    print(f"Indice: {indice} , Valor: {valor}")
# Exemplo de manipulação da lista:
    if lista_enumerate[indice] == "c":
        lista_enumerate[indice] = "o"
    else: 
        lista_enumerate[indice] = "x"
print(lista_enumerate)