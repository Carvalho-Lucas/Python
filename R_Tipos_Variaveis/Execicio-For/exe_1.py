#Execício 01

nome = "Lucas"
idade = 28

casado = input("Você é casado ? (s/n): ").lower()
if casado == "s":
    print(True)
else:
    print(False)


print("\n")
#-----------------------------------------------------#
#Execício 02

num1 = 2
num2 = 3

result = num1 + num2
print("Soma: ", result)
result = num1 - num2
print("Subtração: ", result)
result = num1 * num2
print("Multiplicação: ", result)
result = num1 / num2
print("Divisão: ", result)
result = num1 % num2
print("Resto da divisão: ", result)


print("\n")
#-----------------------------------------------------#
#Execício 03

nome_completo = "Lucas Pereira de Carvalho"
split = nome_completo.split(" ")
primero_nome = split[0]
print("Split - >",primero_nome)
print("Nome MAIUSCULO: ",nome_completo.upper())
print("Nome Minusculo: ",nome_completo.lower())
print(nome_completo.lower().count("a"))

print("\n")
#-----------------------------------------------------#
#Execício 04

idade = 12

if idade >= 18:
    print("Pode dirigir!!")
elif 12 <= idade <= 17:
    print("Adolescente")
else:
    print("Criança")


print("\n")
#-----------------------------------------------------#
#Execício 05

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Digite sua cidade: ")

print(f"Seu nome é: {nome}, você tem {idade} anos , mora na cidade de {cidade}")


print("\n")
#-----------------------------------------------------#
#Execício 06

cores = ["amarelo", "vermelho", "azul", "verde", "branco"]
print("A primeira cor da lista é:", cores[0])
cores.append("cinza")
print("Lista atualizada com nova cor: ", cores)

print("\n")
#-----------------------------------------------------#
#Execício 07

comida_favorita = ("Pizza", "Hamburger", "Hot Dog")
for indice, comida in enumerate(comida_favorita):
    print(f"Índice {indice} = Comida: {comida}")

result = comida_favorita.index("Pizza")
print("O indice do item pizza é: ",result)


print("\n")
#-----------------------------------------------------#
#Execício 08

carro = {"marca": "Nissan", "ano": "2025", "cor": "preto"}
chaves = list(carro.keys())
print("Apenas chaves: ",chaves)
valores = list(carro.values())
print("Apenas valores: ",valores)
itens = list(carro.items())
print("Método para retornar uma lista de tuplas (chave, valor): ", itens)
carro["cor"] = "branco"
print(carro)


print("\n")
#-----------------------------------------------------#
# Exercício 09 (com enumerate) - Verificar números pares e ímpares

numeros = [1, 2, 3, 4, 5]

print("Lista de números inteiros:", numeros)

for indice, valor in enumerate(numeros):
    if valor % 2 == 0:
        print(f"Índice: {indice} | Número par: {valor}")
    else:
        print(f"Índice: {indice} | Número ímpar: {valor}")


print("\n")
#-----------------------------------------------------#
# Exercício 10


for numero in range(0,11):
    print("Numero", numero)

tarefas = ["Estudar", "Trabalhar", "Jogar"]

print("Lista de Tarefas:", tarefas)

for indice, valor in enumerate(tarefas):
    print(f"índice: {indice} | Valor {valor}")


print("\n")
#-----------------------------------------------------#
# Exercício 11

alunos = [
     {"nome": "Lucas", "idade": 28, "cidade": "MG"},
     {"nome": "Luiz", "idade": 27, "cidade": "MG"},
     {"nome": "Fábio", "idade": 33, "cidade": "MG"},
]

print("Lista de Alunos:")
for indice, aluno in enumerate(alunos):
    print(f"{indice} - Nome: {aluno['nome']} | Idade: {aluno['idade']} | Cidade: {aluno['cidade']}")

selecao = int(input("\nDigite o número do aluno que deseja visualizar: "))
aluno = alunos[selecao]  # <-- AQUI

print(f"\n--- Dados do aluno selecionado ---")
print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno['idade']}")
print(f"Cidade: {aluno['cidade']}")

# Pergunta se quer atualizar
atualizar = input("\nDeseja atualizar os dados desse aluno? (s/n): ").lower()

if atualizar == "s":
    novo_nome = input("Digite o novo nome (ou pressione Enter para manter): ")
    nova_idade = input("Digite a nova idade (ou pressione Enter para manter): ")
    nova_cidade = input("Digite a nova cidade (ou pressione Enter para manter): ")

     # Atualiza apenas se o campo não estiver vazio
    if novo_nome:
        aluno["nome"] = novo_nome
    if nova_idade:
        aluno["idade"] = int(nova_idade)
    if nova_cidade:
        aluno["cidade"] = nova_cidade

    print("\n✅ Dados atualizados com sucesso!")
    print(alunos)
else:
    print("\nNenhuma alteração realizada.")