import random

class JogoAdivinhacao:
    def __init__(self):
        self.numero_secreto = random.randint(1, 100)
        self.tentativas = 0
        self.max_tentativas = 10

    def iniciar_jogo(self):
        print("Bem-vindo ao Jogo de Adivinhação!")
        print("Tente adivinhar o número secreto entre 1 e 100.")

        while self.tentativas < self.max_tentativas:
            try:
                palpite = int(input("Digite seu palpite: "))
            except ValueError:
                print("Por favor, digite um número válido.")
                continue

            self.tentativas += 1

            if palpite < self.numero_secreto:
                print("Tente um número maior.")
            elif palpite > self.numero_secreto:
                print("Tente um número menor.")
            else:
                print(f"Parabéns! Você acertou o número secreto ({self.numero_secreto}) em {self.tentativas} tentativas.")
                break

        if self.tentativas == self.max_tentativas:
            print(f"Fim do jogo. Você esgotou suas {self.max_tentativas} tentativas. O número secreto era {self.numero_secreto}.")

# Criar uma instância da classe e iniciar o jogo
jogo = JogoAdivinhacao()
jogo.iniciar_jogo()
