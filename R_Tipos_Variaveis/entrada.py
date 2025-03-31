idade = int(input("Digite sua idade:"))

if idade >= 18:
    print(f"Idade digitada: {idade} - Maior de idade")
elif idade >= 12:
    print(f"Idade digitada: {idade} - Adolescente de idade")
else:
    print(f" {idade} - Você é menor de idade.")

mensagem = f"Pode tirar carteira de habilitação, sua idade é: {idade}" if idade >= 18 else "Você não tem idade suficiente para tirar carteira!"
print(mensagem)
