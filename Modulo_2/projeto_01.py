import random

#Jogo de combate em turno (Heroi / inimigo) 
#Personagem: Classe Pai
#Heroi: Controlado pelo usuário
#Inimigo: Controlado pelo usuário

class Personagem():
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel #Heroi com nível mais alto da mais dano
    
    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self): #Método criado na classe pai, uma vez que é implementado tanto para Heroi quanto para Inimigo.
        return f"Nome: {self.get_nome()} \nNível: {self.get_nivel()} \nVida: {self.get_vida()}"
    
    def receber_dano(self, dano):
        self.__vida -= dano
        if self.__vida <= 0:
            self.__vida = 0

    def atacar(self, alvo):
        dano = random.randint(self.get_nivel () *2, self.get_nivel () *4)#dano baseado no nível
        alvo.receber_dano(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano")

class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()} \nHabilidade: {self.get_habilidade()}\n "
    
    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel () *5, self.get_nivel () *8)#dano baseado no nível
        alvo.receber_dano(dano)
        print(f"{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} causando {dano} de dano!")

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo 

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()} \nTipo: {self.get_tipo()}\n "
    
class Jogo: 
    """ Classe que realiza gestão do jogo"""

    def __init__(self):
        self.heroi = Heroi(nome="Batman", vida = 100, nivel =5, habilidade="Super força")
        self.inimigo =  Inimigo(nome="Coringa", vida = 80, nivel =5, tipo="Fumaça")

    def iniciar_batalha(self):
        """ Fazer a gestão da batalha em turnos"""
        #Heroi morro ou inimigo morre, enquanto tiver vida, jogo continua.
        print("Iniciando a batalha!")

        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos personagens: ")
            print(f"Heroi: {self.heroi.exibir_detalhes()}")
            print(f"Inimigo: {self.inimigo.exibir_detalhes()}")

            input("Pressione Enter para atacar...")
            escolha = input("Escolha (1- Ataque normal, 2- Ataque Especial): ")

            if escolha == '1':
                self.heroi.atacar(self.inimigo)
            elif escolha =='2':
                self.heroi.ataque_especial(self.inimigo)
            else: "Escolha inválida!"

            if self.inimigo.get_vida() >0:
                #Inimigo ataca heroi
                self.inimigo.atacar(self.heroi)
        
        if self.heroi.get_vida() >0:
            print("Parabens!! Heroi vence a batalha!")
        else:
            print("O inimigo venceu!!") 

jogo = Jogo() #Cria o jogo com os personagens
jogo.iniciar_batalha() # Inicia batalha