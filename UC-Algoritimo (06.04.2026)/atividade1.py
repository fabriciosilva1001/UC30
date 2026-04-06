import random

def jogar():
    alvo = random.randrange(1, 101)
    tentativas = 0
    resposta = ""

    print("Descubra o número escondido.")

    while resposta != "certo":
        chute = int(input("Seu palpite: "))
        tentativas += 1

        if chute == alvo:
            resposta = "certo"
        elif chute < alvo:
            resposta = "maior"
        else:
            resposta = "menor"

        if resposta != "certo":
            print(resposta)

    print("Você acertou em", tentativas, "tentativas")

jogar()