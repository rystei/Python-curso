print("**********************************")
print("Bem vindo ao jogo de adivinhação !")
print("**********************************")

numero_secreto = 30
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("digite um numero: ")
    print("você digitou, ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("você acertou o numero!")
    else:
        if (maior):
            print("você errou o numero! :(, seu chute foi maior que o numero secreto ")
        elif (menor):
            print("você errou o numero! :(, seu chute foi menor que o numero secreto ")

    rodada = rodada + 1
print("Acabou o jogo!")
