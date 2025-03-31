"""
🧩 O que é um dicionário?

É uma coleção de dados estruturados em pares: chave → valor.
Pensa literalmente num dicionário de palavras:

palavra (chave) → significado (valor)

-> Coleção não ordenada
"""

pessoa = {"nome": "Lucas", "idade": 27, "cidade": "MG"}
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])
print("\n")

#🆕 Adicionando novos pares
pessoa["sobrenome"] = "Carvalho"
print("Método para ADICIONAR chave/valor(par) SOBRENOME:", pessoa)

#✏️ Atualizando valores
pessoa["idade"] = 28
print("Método para ATUALIZAR chave/valor(par) IDADE:", pessoa)

#🗑️ Removendo pares
del pessoa["sobrenome"]
print("Método para REMOVER chave/valor(par) SOBRENOME:", pessoa)
print("\n")

#📋 Métodos importantes
#🔹 keys() → retorna uma lista com todas as chaves
#🔹 values() → retorna os valores
#🔹 items() → retorna uma lista de tuplas (chave, valor)

chaves = list(pessoa.keys())
print("Método para retornar todas as chaves: ",chaves)  # ['nome', 'idade', 'cidade']

valores = list(pessoa.values())
print("Método para retornar todas os valores: ",valores)  # ['Lucas', 28, 'MG']

itens = list(pessoa.items())
print("Método para retornar uma lista de tuplas (chave, valor): ", itens)  #Retorna uma lista de tuplas (chave, valor)
print("Primeiro valor:", itens[0][1])  # valor da 1ª tupla
print("Primeiro valor: %s = %s" % (itens[1][0], itens[1][1]))  # valor da 2ª tupla


