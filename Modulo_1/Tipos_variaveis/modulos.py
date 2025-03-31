#Modulo -> Arquivos que podem ser reutilziados em outros arquivos. 
#print("\n")

print("Exemplo de importação de Modulo padrão")
#import math 
from math import sqrt
#import meu_modulo
from meu_modulo import saudacao, dobro

raiz_quadrada  = int(input("Digite o número para ser cáculado na raiz:"))
resultado = sqrt(raiz_quadrada)
print(f"Raiz quadrada de {raiz_quadrada}, é igual a:", resultado)


print("\n Exemplo de modulo personalizado:")

teste  = int(input("Digite o número para ser cáculado o dobro:"))
resultado_teste = dobro(teste)
print(f"O dobro de {teste} foi de:", resultado_teste)

mensagem = saudacao("Lucas!")
print(mensagem)