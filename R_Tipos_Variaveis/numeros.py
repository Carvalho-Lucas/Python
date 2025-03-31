#Inteiros e floats
numero_inteiro = 3
numero_real = 3.14
numero = 2

#Type() -> Ajuda a ver de qual tipo é a variável.

print("Número inteiro:", type(numero_inteiro))  # Mostra <class 'int'>
print("Número Flutuante:",type(numero_real))     # Mostra <class 'float'>


#Operações básicas... + - * /

resultado = numero_inteiro + numero
print("Operação de soma:", resultado)

resultado = numero_inteiro - numero
print("Operação de subtração:", resultado)

resultado = numero_inteiro * numero
print("Operação de Multiplicação:", resultado)

resultado = numero_inteiro / numero
print("Operação de Divisão:", resultado)
print("Tipo variável Divisão:",type(resultado))     # Mostra <class 'float'>
print("Valor em inteiro da divisão: ", int(resultado))

#Divisão com resultado inteiro, usa //
divisao = 6//5
print("A divisao com ponto flutuante de 6/5 é :", divisao)

#Modulo = Restante da divisão, utilizado para descobrir se o final do valor é par ou impar
modulo = 5%2
print("O modulo de 5%2 e: ", modulo)
