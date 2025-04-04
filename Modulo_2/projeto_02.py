import random
from abc import ABC, abstractmethod

# Classe base abstrata
class Personagem(ABC):
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def esta_vivo(self):
        return self.__vida > 0

    def receber_dano(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0

    def mostrar_barra_vida(self):
        total = 20
        preenchido = int((self.__vida / 100) * total)
        return f"{self.__nome}: [{'█'*preenchido}{'-'*(total - preenchido)}] {self.__vida} HP"

    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel

    @abstractmethod
    def atacar(self, alvo):
        pass

# Herói
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)
        print(f"{self.get_nome()} atacou com força e causou {dano} de dano.")
        alvo.receber_dano(dano)

    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8)
        print(f"{self.get_nome()} usou {self.__habilidade}! Causou {dano} de dano.")
        alvo.receber_dano(dano)

# Vilão
class Vilao(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 5)
        print(f"{self.get_nome()} ({self.__tipo}) atacou e causou {dano} de dano.")
        alvo.receber_dano(dano)

# Arena do combate
class Arena:
    def __init__(self):
        self.heroi = Heroi("Artemis", 100, 5, "Fúria Celestial")
        self.vilao = Vilao("Skorn", 100, 4, "Sombrio")

    def iniciar_batalha(self):
        print("🔥 Arena dos Campeões 🔥")
        while self.heroi.esta_vivo() and self.vilao.esta_vivo():
            print("\n" + self.heroi.mostrar_barra_vida())
            print(self.vilao.mostrar_barra_vida())

            escolha = input("1 - Ataque Normal | 2 - Ataque Especial: ")
            if escolha == '1':
                self.heroi.atacar(self.vilao)
            elif escolha == '2':
                self.heroi.ataque_especial(self.vilao)
            else:
                print("Opção inválida.")
                continue

            if self.vilao.esta_vivo():
                self.vilao.atacar(self.heroi)

        print("\n⚔️ Fim da Batalha ⚔️")
        if self.heroi.esta_vivo():
            print(f"{self.heroi.get_nome()} venceu a batalha!")
        else:
            print(f"{self.vilao.get_nome()} venceu a batalha!")

# Execução
arena = Arena()
arena.iniciar_batalha()
