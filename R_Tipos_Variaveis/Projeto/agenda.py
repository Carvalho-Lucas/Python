def adicionar_contato(nome_adc, telefone, email, pessoas):
    agenda = {
        "nome": nome_adc,
        "telefone": telefone,
        "email": email,
        "favoritos": False
    }
    pessoas.append(agenda)
    print(f"O contato: {nome_adc}, foi adicionado na lista de contatos!")
    return


def ver_contatos(pessoas):
    if not pessoas:
        print("\n")
        print("Lista de contatos vazia!")
        return

    for indice, agenda in enumerate(pessoas, start=1):
        status = "⭐" if agenda["favoritos"] else "❌"
        nome_pessoa = agenda["nome"]
        telefone = agenda["telefone"]
        email = agenda["email"]
        print(f"Contato: {indice} , Nome: {nome_pessoa} , Telefone: {telefone} , E-mail: {email} -> Favoritos: [{status}] ")
        
    return

def editar_contato(pessoas, indice):
    indice -= 1
    if 0 <= indice < len(pessoas):
        contato = pessoas[indice]
        print("\n")
        print(f"Editando contato: {contato['nome']}")
        contato["nome"] = input("Novo nome: ") or contato["nome"]
        contato["telefone"] = input("Novo telefone: ") or contato["telefone"]
        contato["email"] = input("Novo email: ") or contato["email"]
        print("Contato atualizado com sucesso! Voltando para o Menu...")
    else:
        print("Índice inválido.")
    return

def selecionar_favorito(pessoas, indice_favorito):
    indice_contato_ajustada = indice_favorito - 1
    if indice_contato_ajustada < 0 or indice_contato_ajustada >= len(pessoas):
        print("Índice inválido!")
        return

    if pessoas[indice_contato_ajustada]["favoritos"] == False:
        pessoas[indice_contato_ajustada]["favoritos"] = True
        print(f"Contato {indice_favorito}, adicionado aos favoritos!!! ⭐")
    else: 
        print("O contato já está favoritado!")

def deletar_contato(pessoas, indice_excluido):
    indice = indice_excluido - 1
    if indice < 0 or indice >= len(pessoas):
        print("Índice inválido!")
        return
    contato_removido = pessoas.pop(indice)
    print(f"Contato '{contato_removido['nome']}' removido com sucesso!")
    return
        
pessoas = []

while True:
    print("\n")
    print("Agenda de Contatos:")
    print("1- Adicionar Contato")
    print("2- Ver Contatos")
    print("3- Editar numero do contato")
    print("4- Marcar como favorito")
    print("5- Deletar contato")
    print("6- Sair")

    escolha = int(input("Digite uma opção do Menu acima: "))

    if escolha == 1:
        nome_adc = input("Nome do contato adicionado: ")
        telefone = input("Digite o número de contato do usuário: ")
        email= input("Digite o e-mail do contato: ")
        adicionar_contato(nome_adc, telefone, email, pessoas)
    elif escolha == 2:
        ver_contatos(pessoas)

    elif escolha == 3:
        ver_contatos(pessoas)
        indice_escolha = int(input("Seleciona o número do contato que deseja editar: "))
        editar_contato(pessoas, indice_escolha)

    elif escolha == 4:
        ver_contatos(pessoas)
        indice_favorito = int(input("Informe o número do contato a ser favoritado: "))
        selecionar_favorito(pessoas, indice_favorito)

    elif escolha == 5:
        ver_contatos(pessoas)
        indice_excluido = int(input("Informe o índice do contato que deseja excluir: "))
        deletar_contato(pessoas, indice_excluido)

    elif escolha == 6:
        break
print("Fim projeto")
