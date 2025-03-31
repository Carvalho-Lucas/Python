def adicionar(tarefas, nome_tarefa="Tarefa Padrão"):
    #tarefa: nome tarefa
    #completada: tarefa completa/não

    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"A tarefa de nome: {nome_tarefa} , foi adicionada com sucesso!")
    return

def ver_tarefas(tarefas):
    if not tarefas:
        print("\n")
        print("Lista de tarefas vazia!")
        return
    
    print("\n")
    print("\nLista de tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = " ✅ " if tarefa["completada"] else " ❌ "
        nome_tarefa = tarefa["tarefa"]
        print(f"Tarefa: {indice}. Nome: {nome_tarefa} -> Status: [{status}]")
    return

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome):
    print("\n")
    indice_tarefa_ajustada = indice_tarefa -1

    if 0 <= indice_tarefa_ajustada < len(tarefas):
        tarefas[indice_tarefa_ajustada]["tarefa"] = novo_nome
        print(f"Tarefa: {indice_tarefa}. Atualizada para: {novo_nome}")
    else:
        print("Indice de tarefa inválido!")
    return

def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustada = indice_tarefa -1
    tarefas[indice_tarefa_ajustada]["completada"] = True
    print("\n")
    print(f"Tarefa {indice_tarefa_ajustada}. Marcada como completada!")
    return


def deletar_tarefa_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa["completada"]:
            tarefas.remove(tarefa)
    print("Tarefas completadas removidas!")      
    return

tarefas = []

while True:
    print("\n")
    print("Menu de gerenciamento de tarefas:")
    print("1- Adicionar tarefa")
    print("2- Ver tarefa")
    print("3- Atualizar tarefa")
    print("4- Completar tarefa")
    print("5- Deletar tarefas completadas")
    print("6- Sair")

    escolha = int(input("Digite uma opção do Menu acima: "))

    if escolha == 1:
        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar(tarefas, nome_tarefa)

    elif escolha == 2:
        ver_tarefas(tarefas)

    elif escolha ==3:
        ver_tarefas(tarefas)
        indice_tarefa = int(input("Digite o indice da pessoa para ATUALIZAR nome: "))
        novo_nome = input("Digite o novo nome da pessoa:")
        atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)
    
    elif escolha ==4:
        ver_tarefas(tarefas)
        indice_tarefa = int(input("Digite o indice da pessoa para COMPLETAR STATUS: "))
        completar_tarefa(tarefas, indice_tarefa)

    elif escolha==5:
        deletar_tarefa_completadas(tarefas)
        ver_tarefas(tarefas)

    elif escolha == 6:
        break
print("Fim projeto")
