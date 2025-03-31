class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} está amamentando."
    
class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando."
    
class Morcego(Mamifero, Ave):
    def emitir_som(self):
        #super().emitir_som() Chama a implementação da classe mãe
        return "Morcegos emitem sons ultrassônicos"
    
morcego = Morcego(nome="batman")

# Acessando métodos da classe base "Animal"
print("Nome do morcedo: ", morcego.nome)
print("Som do Morcego:", morcego.emitir_som())

#Acessando métodos das classes Mamifero e Ave

print("Morcedo amamentando:", morcego.amamentar())
print("Morcedo voando:", morcego.voar())
