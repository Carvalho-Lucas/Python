#Bloco utilizado várias vezes

def saudacao(nome):
    print(f"Olá, {nome}!")
nome = input("Digite o nome da pessoa:")
saudacao(nome)


# Função para receber e retornar valor

def quadrado(numero):
    resultado = int(numero) **2
    return resultado

resultado = input("Digite um valor para calcular seu quadrado: ")
resultado_quadrado = quadrado(resultado)
print("Quadrado do numero -> " + resultado + " foi :", resultado_quadrado )


def soma(numero_1, numero_2):
    resultado = numero_1 + numero_2
    return resultado


numero_1 = int(input("Digite o primeiro número para somar: "))
numero_2 = int(input("Digite o segundo número para somar: "))

resultado_soma = soma(numero_1, numero_2)
print("O resultado da soma %s + %s é de %s: " % (numero_1, numero_2, resultado_soma))
    