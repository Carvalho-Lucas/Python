#Eventos que ocorrem durante o código e interrompe o funcionamento do código.
print("Exemplo de excções")
try:
    numero = int(input("Digite um número:"))
    resultado = 10 / numero
except ValueError as e:
    print(f"Erro de value Error: {e}")
    #raise ValueError("Tipo de variável incompativel")
except Exception as e:
    print(f"Erro: {e}")
else:
    print("O resultado foi:", resultado )
finally:
    print("Operaçao Finalizada!")
