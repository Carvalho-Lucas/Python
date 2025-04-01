# Poo -> paradigma que baseia na orietação de objetos (instância de classe - Classe/Objeto)

# Classe - Modulo que define estruta e comportamento do objeto
# Define atributos (propriedades da classe) e métodos ("ações" o que pode realizar)

# Criando classe Pessoa - Exemplo
class Pessoa:
    def __init__(self, nome, idade): #self -> referencia a própria classe - Porta de acesso para usar métodos e atributos
        self.nome = nome
        self.idade = idade

# Criando método dentro da classe Pessoa
    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos"

# Função para criar uma instância da classe Pessoa com input
def criar_pessoa():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    return Pessoa(nome, idade)

# Criando objetos
pessoa1 = criar_pessoa()
pessoa2 = criar_pessoa()

# Chamando o método saudacao
mensagem1 = pessoa1.saudacao()
mensagem2 = pessoa2.saudacao()

print(mensagem1)
print(mensagem2)