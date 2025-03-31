print("Exemplo de captura de excções")
try:
    numero = int(input("Digite um número inteiro:"))
    resultado = 10 / numero
except ValueError as e:
    print(f"Erro de ValueError: {e}")
    raise ValueError("Tipo de variável incompatível!!!") #RAISE: Lança exceção com texto digitado
except Exception as e: #Captura qualquer outro erro (por exemplo, divisão por zero) / Mostra mensagem genérica
    print(f"Erro: {e}") 
else:
    print(f"Resultado: {resultado}") 
    #Else será executado somente se o programa funcionar.
finally:
    print("Saindo do programa!")