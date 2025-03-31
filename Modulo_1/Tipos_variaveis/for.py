#Estrutura de repetição enquanto condição verdadeira FOR / WHILE

print("For utilizando Lista")
lista = [1 , 2 ,3 , 4, 5]

for elemento in lista:
    print(elemento)

print("\n")

print("For utilizando Tupla")
tupla = (1 , 2 ,3 , 4, 5)
for elemento in tupla:
    print(elemento)

print("\n")

print("For utilizando Dicionário -> Chave")
pessoa = {"Nome": "Lucas" , "Idade": 27 , "Cidade": "MG"}
for chave in pessoa.keys():
    print(chave)

print("\n")
print("For utilizando Dicionário -> Valor")
for valor in pessoa.values():
    print(valor)    

print("\n")
print("For utilizando Dicionário -> Lista de tuplas -> Itens")
for itens in pessoa.items():
    print(itens)  

print("\n")
print("For utilizando Dicionário -> Itens")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")  


#RANGE() Intervalo numérico em um formato de lista
print("\n")
for numero in range(5):
    print("Número gerado com range:", numero)

print("\n")
#Lista mutável com for + Range() + Len()  ->>>> Manipulação de Lista <<<<-
print("Função range + len")
lista = [1 , 2 ,3 , 4, 5]
for indice in range(0, len(lista)):
    print(f"Indice: {indice} , Elemento:{lista[indice]}")  

print("\n")
#Lista mutável com for + Range() + Len() + Condicional  ->>>> Manipulação de Lista <<<<-
print("Função range + len + Condicional")
lista = [1 , 2 ,3 , 4, 5]
for indice in range(0, len(lista)):
    if indice == 3:
        lista[indice] = 5
    else:
        lista[indice] = 0
print(lista) 

#Enumerate  ->>> Mesmo resultado da anterior, mas só passa a lista.

lista_enumerate = ["a","b","c"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}:{valor}")
    if indice ==1:
        print(" Passei pelo Indice 1")