print("**********************************")
print("Bem vindo ao jogo de adivinhação !")
print("**********************************")

numero_secreto = 30

chute_str = input("digite um numero: ")
print("você digitou, ", chute_str)
chute = int(chute_str)

if numero_secreto == chute:
    print("você acertou o numero!")
else:
    print("você errou o numero! :( ")

print("Acabou o jogo!")
