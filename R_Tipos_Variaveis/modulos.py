# Modulos - Bloco de código que podem ser reutilizados

print("Exemplo de importação de modulo padrão: ")
from math import sqrt


raiz_quadrada = int(input("Digite número para raiz quadrada:"))
result = sqrt(raiz_quadrada)
print(f"A raiz quadrada de {raiz_quadrada} é {result}")
print("\n")
"""Módulo Personalizado"""

print("Exemplo de importação de modulo personalizado: ")

from meu_modulo import saudacao, dobro

nome = input("Digite seu nome:")
mensagem = saudacao(nome)
print(mensagem)
print("\n")

num = int(input("Digite um número para calcular dobro:"))
result = dobro(num)
print(f"O resultado do dobro de {num} e: {result}")