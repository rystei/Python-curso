print("**********************************")
print("Bem vindo ao jogo de adivinhação !")
print("**********************************")

numero_secreto = 30

chute = input("digite um numero: ")

print("você digitou, ", chute)

if chute == numero_secreto:
    print("você acertou o numero!")
else:
    print("você errou o numero :( ")

print("Acabou o jogo")
