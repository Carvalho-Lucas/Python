# Lista de estudantes
estudantes = []

# Criar 3 cadastros
for _ in range(3):
    pessoa = {}
    pessoa["nome"] = input("Digite o nome do aluno: ")
    pessoa["idade"] = int(input("Digite a idade: "))
    pessoa["cidade"] = input("Digite a cidade: ")
    estudantes.append(pessoa)

# Mostrar todos os alunos cadastrados
print("\n--- Alunos cadastrados ---")
for indice, estudante in enumerate(estudantes):
    print(f"{indice} - {estudante['nome']}")

# Selecionar aluno por índice
selecao = int(input("\nDigite o número do aluno que deseja visualizar: "))
aluno = estudantes[selecao]

print(f"\n--- Dados do aluno selecionado ---")
print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno['idade']}")
print(f"Cidade: {aluno['cidade']}")

# Perguntar se quer alterar dados
alterar = input("\nDeseja alterar os dados? (s/n): ").lower()
if alterar == "s":
    aluno["nome"] = input("Novo nome: ")
    aluno["idade"] = int(input("Nova idade: "))
    aluno["cidade"] = input("Nova cidade: ")

# Mostrar dados atualizados
print("\n--- Dados atualizados ---")
print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno['idade']}")
print(f"Cidade: {aluno['cidade']}")
