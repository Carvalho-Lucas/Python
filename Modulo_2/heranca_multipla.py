# Herança múltipla permite que uma classe herde de duas ou mais ao mesmo tempo.
# A classe Morcego herda comportamentos de Mamifero (amamentar) e Ave (voar),
# além de poder sobrescrever métodos da classe base (emitir_som).

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} está amamentando."

class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando."
    
#Morcego é mamifero e também um animal... Implementa as duas classes, logo:

class Morcego(Mamifero, Ave):
    def emitir_som(self):
        return f"Ultra Som -> Morcego"
    
morcego = Morcego(nome="Batman")

#Acessando método da classe base animal

print("Nome do Morcego:", morcego.nome)
print("Som do morcego:", morcego.emitir_som())

#Acessando métodos da classes Mamifero e Ave

print("Morcedo amamentando:", morcego.amamentar())
print("Morcego voando:", morcego.voar())
