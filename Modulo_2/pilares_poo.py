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

dog = Cachorro(nome="Rex")
cat = Gato(nome="Felix")
print("\n")

print("Exemplo de Polimorfismo: ")
animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")

print("\n")
print("Exemplo de encapsulamento") #Uso de atributos privados para proteger os dados de código


# Encapsulamento -> Protege dados internos da classe.
# O atributo __saldo é privado e só pode ser acessado/modificado pelos métodos da classe.
# Isso evita alterações indevidas ou inseguras de fora da classe.

class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo #atributo privado -> apenas métodos da classe bancária tem acesso a saldo(privado)

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
    
    def consultar_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(saldo=1000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()} ")
conta.depositar(valor=500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()} ")
conta.depositar(valor=-500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()} ")
conta.sacar(valor=200)
print(f"Saldo da conta bancária: {conta.consultar_saldo()} ")


"""
Abstração -> Molde para construir classe - Classe abstrata não 

É tipo o “manual” que obriga as subclasses a implementarem algo

"""
print("\n")
print("Exemplo de abstração: ")
from abc import ABC, abstractmethod

class Veiculo(ABC):
    
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self):
        pass

    def ligar(self):
        #Ligação do carro
        return "Carro Ligado usando chave"
    
    def desligar(self):
        return "Carro desligado usando chave"

carro_amarelo  = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())
