#Organização de programas em objetos
"""
Classe Pessoa -> Descreve atributos/propriedades e métodos

DEF -> Quando está fora de uma classe é uma função 
DEF -> Quando está dentro de uma classe é um método
"""

class Pessoa: 
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    
    def saudacao(self):
        return f"Seja Bem-Vindo!!\n"

# Objetos -> instância da classe -> respeita atributos e métodos da classe
pessoa1 = Pessoa("Lucas", 27)
mensagem = pessoa1.saudacao()

nome = input( f"{mensagem} Objeto criado -> {pessoa1.nome}, idade: {pessoa1.idade}")

pessoa2 = Pessoa("Rodrigo", 22)
nome = input( f"{mensagem} Objeto criado -> {pessoa2.nome}, idade: {pessoa2.idade}")

