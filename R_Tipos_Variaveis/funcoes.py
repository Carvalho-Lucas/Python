# Bloco de código reutilizável

def saudacao():
    nome = input("Digite o seu nome: ")
    print(f"Olá {nome}")

print("\nChamando a função saudacao:")
saudacao()

# Função com retorno -  Quadrado
def quadrado():
    numero = int(input("Digite um número para calcular o quadrado: "))
    result =  numero **2
    return result

print("\nChamando a função Quadrado:")
resultado = quadrado()
print(f"Resultado da Função quadrado: {resultado}")


#Função com multiplos parametros

def soma(numero_1, numero_2):
    resultado = numero_1 + numero_2
    return resultado

print("\nChamando a função Soma:")
num1 = int(input("Digite o primeiro número para soma: "))
num2 = int(input("Digite o segundo número para soma: "))
resultado = soma(num1, num2)
print(f"Resultado da Função soma: {resultado}")