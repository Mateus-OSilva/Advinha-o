print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3

while (rodada <= total_de_tentativas):
    print("Tentativa {} de {} ".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Voce digitou ", chute_str)
    chute = int(chute_str)

    if(chute < 1):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou")

    else:
        if (maior):
            print("Você errou, o seu chute foi maior do que o número secreto.")
        elif (menor):
            print("Voce errou!, o seu chute foi menor do que o número secreto")

    rodada = rodada + 1

    print("Fim do jogo")
