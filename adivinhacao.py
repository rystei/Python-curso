print("**********************************")
print("Bem vindo ao jogo de adivinhação !")
print("**********************************")

numero_secreto = 30

chute_str = input("digite um numero: ")

print("você digitou, ", chute_str)

chute = int(chute_str)

acertou = chute == numero_secreto
maior   = chute > numero_secreto
menor   = chute < numero_secreto

if acertou:
    print("você acertou o numero!")
else:
    if (maior):
        print("você errou o numero! :(, seu chute foi maior que o numero secreto ")
    if (menor):
        print("você errou o numero! :(, seu chute foi menor que o numero secreto ")

print("Acabou o jogo!")
