#Declaração

nome_completo = "Lucas Carvalho"
nome_completo_aspas = """Lucas
Carvalho"""
nome_completo_quebra = "Lucas \
Carvalho"

nome= "Lucas"
sobrenome = "Carvalho"

#Formatação 

print ("Nome completo (1a Forma):", nome_completo)
print ("Nome completo (2a Forma):"+ nome_completo)
print ("Nome completo (3a Forma):"+"Lucas" + "Carvalho")
print ("Nome completo (4a Forma):"+"Lucas", "Carvalho")
print ("Nome completo (5a Forma):", nome_completo_aspas)
print ("Nome completo (6a Forma):", nome_completo_quebra)
print ("Nome completo (7a Forma) com uma string: %s" % nome_completo )
print ("Nome completo (8a Forma) com dua strings: %s %s" % (nome, sobrenome))
print (f"Nome completo (8a Forma) com f: {nome} {sobrenome}")
print ("Nome completo (9a Forma) com format: {} {}".format(nome, sobrenome))



print("\n")
print("Aula de funções: \n")

"""
Função que transforma letras para maúsculo/minusculo  -> .upper() ou .lower()

OBS: Conteúdo imutável, não altera o valor da variável. Apenas pega o conteúdo e transforma. 
"""
print("Função .UPPER: ",nome.upper())
print("Função .LOWER: ",nome.lower())

print("\n")
print("Função para verificar qual foi a primeira letra digitada. [posicao]")
print("Primeira letra do nome: ", nome[0])
print("\n")

print("\n")
#Função para verificar ocorrência de determinada letra. -> Count()
print("Função .Count: ",nome_completo.upper().count("C"))


print("\n")
#Função para encontrar a posição do parâmetro pesquisado
print("Função .Count: ",nome_completo.find("s"))


print("\n")
#Função para converter string para bits
print("Função para converter em bits: ", nome.encode())
#print(nome.encode().decode()) -> decode() para decodificar algo.

print("\n")
#Função para realizar substituição de caractere .replace()
# Função muito utilizada para tratamento de dados. Exemplo: remover traço da lista telefonica;


print("Função para realizar substituíção de caracter .REPLACE() :", nome_completo.replace("c", "1" ))
telefone = "(31)99457-0792"
print("Telefone sem replace: ", telefone)
print("Removendo o traço ' - ' do número de telefone: ", telefone.replace("-", ""))

print("\n")
#Função JOIN() - separador a cada caractere
print("Função para inserir separador em string")
print("-".join("Lucas"))

print("\n")
#Função SPLIT, divide caracter em lista com base em um alvo 

print("Função SPLIT que realizada divisão de variável através de uma propriedade passada como alvo: ", nome_completo.split(" "))

print("\n")
teste_ruido = "xTeste Ruidox"
#Função que realiza remoção de caracter informado como "ruído" no inicio ou final da variável
#Pode ser removido somente do inicio, quanto do final. Sendo RSTRIP para final e LSTRIP para inicio
print("Variável escrita com erro, letra 'x':", teste_ruido)
print("Função STRIP, responsável por remover ruído: ", teste_ruido.strip("x"))

print("\n")
#Acrescimo de comparadores: IN e NOT IN - startswith para comparar se variável começa como esperado.
print(nome_completo.startswith("Lucas"))

print("Comparando se existe o caractere pesquisado 'Lu' na variável nome com termo -> IN: ", "Lu" in nome)
print("Comparando se NÃO existe o caractere pesquisado 'abc' na variável nome com termo ->  NOT IN: ", "abc" not in nome)

