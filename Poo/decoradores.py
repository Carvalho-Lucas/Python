#Função utilizada para realizar validação. Verificar se um usuário está ou nao logado no sistema.

from typing import Any

def meu_decorador(func):
    def wrapper():
        print("Antes da funçao")
        func()
        print("Depois da função")
    return wrapper

@meu_decorador
def minha_funcao():
    print("MInha função foi chamada")

minha_funcao()


class MeuDecoradorDeClasse:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self) -> Any:
        print("Antes da função - CLASSE")
        self.func()
        print("Depois da função - CLASSE")

@MeuDecoradorDeClasse
def segunda_funcao():
    print("Segunda funcao foi chamada")

segunda_funcao()