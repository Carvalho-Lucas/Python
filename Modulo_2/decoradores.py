# Decoradores permitem "embrulhar" funções com outras funcionalidades.
# Podem ser feitos com função ou classe.
# São usados para adicionar comportamentos antes/depois de funções, como validações.

def meu_decorador(func):
    def wrapper(): #embrulho -> embrulha a função permitindo fazer algo antes e dps da função
        print("Antes da função ser chamada")
        func()
        print("Depois da fuinção ser chamada")
    return wrapper

@meu_decorador
def minha_funcao():
    print("Minha função foi chamada")
    
minha_funcao()

class MeuDecoradorDeClasse:
    def __init__(self, func):
        self.func = func

    def __call__(self): 
        print("Antes da função ser chamada - Decorador Classe ")
        self.func()
        print("Despois da função ser chamada - Decorador Classe")

@MeuDecoradorDeClasse
def segunda_funcao():
    print("Segunda função foi chamada")

segunda_funcao()


"""import time  # usado para pausar execução

# Decorador com limite de tentativas e bloqueio temporário
def verifica_senha(func):
    def wrapper(*args, **kwargs):
        while True:
            tentativas = 0
            while tentativas < 3:
                senha = input("Digite a senha para acessar: ")
                if senha == "1234":
                    print("Acesso permitido!")
                    return func(*args, **kwargs)
                else:
                    tentativas += 1
                    print("Senha incorreta.")
            
            print("Número excessivo de tentativas. Acesso bloqueado por 10 segundos.")
            time.sleep(10)  # aguarda 10 segundos antes de permitir nova rodada
            print("Você pode tentar novamente.\n")
    return wrapper

# Função protegida
@verifica_senha
def acessar_dados_sigilosos():
    print("Mostrando dados secretos do sistema...")

# Chamada
acessar_dados_sigilosos()
"""