
# === Função para adicionar tarefa na lista ===
def adicionar(tarefas, nome_tarefa="Tarefa Padrão"):
    # Cria um dicionário com nome e status de conclusão
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    # Adiciona esse dicionário à lista de tarefas
    tarefas.append(tarefa)
    # Exibe mensagem de confirmação
    print(f"A tarefa de nome: {nome_tarefa} , foi adicionada com sucesso!")
    return

# === Função para exibir a lista de tarefas ===
def ver_tarefas(tarefas):
    # Se a lista estiver vazia, avisa e sai da função
    if not tarefas:
        print("\n")
        print("Lista de tarefas vazia!")
        return
    
    print("\nLista de tarefas:")
    # Percorre a lista com índice começando do 1
    for indice, tarefa in enumerate(tarefas, start=1):
        # Define ícone de status com base no campo 'completada'
        status = "✅" if tarefa["completada"] else "❌"
        nome_tarefa = tarefa["tarefa"]
        # Exibe cada tarefa formatada
        print(f"Tarefa: {indice}. Nome: {nome_tarefa} -> Status: [{status}]")
    return

# === Função para atualizar o nome de uma tarefa específica ===
def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome):
    print("\n")
    # Ajusta o índice informado pelo usuário (começa do 1) para o índice da lista (começa do 0)
    indice_tarefa_ajustada = indice_tarefa - 1

    # Verifica se o índice é válido
    if 0 <= indice_tarefa_ajustada < len(tarefas):
        # Atualiza o nome da tarefa
        tarefas[indice_tarefa_ajustada]["tarefa"] = novo_nome
        print(f"Tarefa: {indice_tarefa}. Atualizada para: {novo_nome}")
    else:
        print("Indice de tarefa inválido!")
    return

# === Lista principal de tarefas ===
tarefas = []

# === Laço principal de execução (menu) ===
while True:
    print("\nMenu de gerenciamento de tarefas:")
    print("1- Adicionar tarefa")
    print("2- Ver tarefa")
    print("3- Atualizar tarefa")
    print("4- Completar tarefa")
    print("5- Deletar tarefas completadas")
    print("6- Sair")

    # Recebe a escolha do usuário
    escolha = int(input("Digite uma opção do Menu acima: "))

    # Adiciona uma nova tarefa
    if escolha == 1:
        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar(tarefas, nome_tarefa)

    # Mostra todas as tarefas
    elif escolha == 2:
        ver_tarefas(tarefas)

    # Atualiza o nome de uma tarefa
    elif escolha == 3:
        ver_tarefas(tarefas)
        indice_tarefa = int(input("Digite o indice da pessoa para atualizar nome: "))
        novo_nome = input("Digite o novo nome da pessoa:")
        atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)

    # Encerra o programa
    elif escolha == 6:
        break

# Mensagem final
print("Fim projeto")
