# Estrutura parecida com lista, mas imutável (não dá pra alterar depois de criada).
# É ordenada → os elementos mantêm a ordem de inserção.


minha_tupla = (1, 2, 3, 4)
print("Tupla na posição 01: ",minha_tupla[1])   # Resultado: 2
print("Tupla na ÚLTIMA posição: ",minha_tupla[-1])  # Resultado: 4 (último elemento)



# Métodos úteis na tupla
#✅ COUNT(valor)
#Informa a quantidade de vezes que ocorre o valor buscado.

result = minha_tupla.count(2)  # Resultado: 2
print("Método COUNT -> Conta quantas vezes o elemento pesquisado aparece.",result)

#✅ INDEX(valor)
#Informa o indice em que ocorre o valor buscado.
result = minha_tupla.index(3)  # Resultado: 1 (primeiro "2" está no índice 1)
print("Método COUNT -> Conta quantas vezes o elemento pesquisado aparece.",result)