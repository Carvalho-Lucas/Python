#Execução de bloco de código por condição
#if, elif e else

idade = 11
print("Exemplo de comando IF:")

if idade >=18:
    print (f"Idade: {idade} - Maior de idade")
elif idade >= 12: 
    print (f"Idade: {idade} - Adolescente")
else:
    print (f"Idade: {idade} - Menor de idade")

mensagem = "Pode tirar carteira de habilitação" if idade >= 18 else "Você não tem idade suficiente para tirar carteira!"
print(mensagem)
