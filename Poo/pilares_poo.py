# Herança -> Herda atributos e métodos da classe mae

class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def andar(self):
        print("O animal andou!")
        return

    def emitir_som(self):
        pass

#Polimorfismo -> Método implementado pela classe mãe, mas com comportamento diferente 
class Cachorro(Animal):
    def emitir_som(self):
        return "Au, Au"
    
class Gato(Animal):
    def emitir_som(self):
        return "Miau!"
    
dog = Cachorro(nome="Ciclope")
cat = Gato(nome="Felix")

print("Uso de Polimorfismo")
animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")

#Encapsulamento -> Somente os métodos pertencentes a classe Conta Bancaria que utiliza.
#Em python, atributos privados são representados por dois undelines -> __


print("\nExemplo de encapsulamento")
class ContaBancaria:
    def __init__(self,saldo) -> None:
        self.__saldo = saldo #Atributo Privado

    def depositar(self, valor):
        if valor > 0:
           self.__saldo +=valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
    
    def consulta_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(saldo=1000)

print(f"\nSaldo da conta bancária: {conta.consulta_saldo()}")
conta.depositar(valor=500)

print(f"Depósito em conta bancária: {conta.consulta_saldo()}")
conta.depositar(valor=-1000) #Nao funciona devido a implementação da condicional > 0

conta.sacar(valor=200)
print(f"Valor sacado da conta bancária: {conta.consulta_saldo()}")


conta_do_ze = ContaBancaria(saldo=100)

print(f"\nSaldo da conta bancária do zé: {conta_do_ze.consulta_saldo()}")
conta_do_ze.depositar(valor=500)
print(f"Valor em conta bancária: {conta_do_ze.consulta_saldo()}")


print("\nExemplo de Abstração")
#Abstraçao -> "molde" ou um projeto incompleto que serve de base para outras classes. 
# Ela é como uma receita que dá a ideia geral do que precisa ser feito, mas não fornece todos os detalhes

from abc import ABC, abstractmethod

class Veiculo(ABC):

    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def acelerar(self):
        pass 
    @abstractmethod
    def frear(self):
        pass

class Carro(Veiculo):
    def __init__(self) -> None:
        pass

    def ligar(self):
        return "Carro Ligado"
    
    def acelerar(self):
        return "Veículo em 50KM/H"
    
    def frear(self):
        return "Veículo em 30KM/H"
carro_amarelo = Carro()

print(carro_amarelo.ligar())
print(carro_amarelo.acelerar())
print(carro_amarelo.frear())

