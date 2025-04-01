""" Herança ->
Permite que uma classe "filha" herde atributos e métodos de uma classe "pai",
evitando repetição de código e facilitando a reutilização.
No exemplo abaixo, Cachorro e Gato herdam de Animal,
e cada um implementa seu próprio método emitir_som().
"""
print("Classe de exemplo - Herança")

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def andar(self):
        print(f"O animal {self.nome} andando")
        return
    
    def emitir_som(self):
        pass
    
class Cachorro(Animal):

    def emitir_som(self):
        return "Au, Au!" #Polimorfismo -> Utiliza o mesmo método usado na classe mãe, mas é reemplementado com comportamento diferente
    #Cachorro = Au, au / Gato = Miau, Maiu.
    
class Gato(Animal):
    
    def emitir_som(self):
        return "Miau, Miau!" #Polimorfismo -> Utiliza o mesmo método usado na classe mãe, mas é reemplementado com comportamento diferente
    #Cachorro = Au, au / Gato = Miau, Maiu.