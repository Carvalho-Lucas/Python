#Coleção não ordenada de pares, chaves e valores

pessoa = {"nome": "Lucas" , "idade": 27 , "cidade": "MG"}

print("Meu dicionário 1 de exemplo: ", pessoa)

#Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])


print("\n")


pessoa["sobrenome"] = "Carvalho"
print("Sobrenome:", pessoa["sobrenome"])
print("Dicionário 2 após adicionar sobrenome -> (Chave/Valor): ", pessoa)


print("\n")

#Para atualizar um par de chave/valor, somente é preciso atribuir novo valor para a variável do dicionário.
pessoa["idade"] = "28"
print("Idade Atualizada:", pessoa["idade"])


print("\n")
#Para remover uma chave/valor da lista, utiliza-se o DEL
print("Removendo a chave/valor 'Sobrenome':")

del pessoa["sobrenome"]
print("Meu dicionário 3, sem sobrenome: ", pessoa)



print("\n")
#Método Keys() -> retorna lista de chaves -> Para acessar lista, deve converter as keys em lista com 'list' ,  values() retorno de todos os valores em formato de lista
#items() -> Lista de tuplas contendo todas pares, chaves e valor

chaves = list(pessoa.keys())
print("Chaves do dicionário 1", chaves)
print("Acessando primeira chave do dicionário:", chaves[0])

valores = list(pessoa.values())
print("Valores do dicionário 1", valores)
print("Acessando primeiro valor do dicionário:", valores[0])

itens = list(pessoa.items())
print("Pares, chaves e valor do dicionário: ", itens)
print("Acessando primeiro valor do dicionário com Itens:", itens[0][1])
print("Primeira Chave/valor: %s = %s" % (itens[0][0], itens[0][1]))
print("Segunda Chave/valor: %s = %s" % (itens[1][0], itens[1][1]))
print("Terceira Chave/valor: %s = %s" % (itens[2][0], itens[2][1]))