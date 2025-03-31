#Deve-sse Utilizar o comando "INPUT" para realizar entrada de dados.
idade = int(input("Digite a idade desejada: "))
if idade >=18:
    print("Você é maior de idade!")
elif idade >= 12: 
    print("Você é um adolescente!")
else:
    print("Você é menor de idade!")

mensagem = "Pode tirar carteira de habilitação" if idade >= 18 else "Você não tem idade suficiente para tirar carteira!"
print(mensagem)