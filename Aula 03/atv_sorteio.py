# importar biblioteca random
import random

# definir variavel com numero aleatorio

numero_aleatorio = random.randint(0, 50)

# definir contador para tentativas
tentativas = 0


# criar loop
# usuario realizar uma tentativa
# incrementa valor para tentativas +1
# se a tentativa do usuario for menor que o numero, printa tente um maior
# se for maior, printa tente um menor
# senao printa que acertou e com quantas tentativas, e quebra o loop.

while True:

    chute = int(input("Insira seu palpite: "))

    if chute < numero_aleatorio:
        print("O número sorteado é maior...")
        tentativas +=1
    
    if chute > numero_aleatorio:
        print("O número sorteado é menor...")
        tentativas +=1

    if chute == numero_aleatorio:
        print("Parabens, você ganhou um curso gratuito na plataforma codigos do bem.")
        print("Você acertou em {} tentativas".format(tentativas))
        break