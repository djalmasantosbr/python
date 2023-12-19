import random
import os

placar_humano = 0
placar_maquina = 0


lance = ['Papel','Pedra', 'Tesoura']


def jokepo(voce,computador):
    if (voce == 'Papel' and computador == 'Papel') or (voce == 'Pedra' and computador == 'Pedra') or (voce == 'Tesoura' and computador == 'Tesoura')  :
        resultado = "Empatou..."
    elif voce == 'Papel' and computador == 'Pedra':
        resultado = "Você ganhou"    
    elif voce == 'Pedra' and computador == 'Tesoura':
        resultado = "Você ganhou"  
    elif voce == 'Tesoura' and computador == 'Papel':
        resultado = "Você ganhou"     
    else:
        resultado = "Computador ganhou"  
    return resultado


    
while True:
    
    print("============================================")
    print("Bem vindo ao jogo de Papel, Pedra ou Tesoura")
    print("============================================")
    print("")
    print("PLACAR:")
    print("Você: {}".format(placar_humano))
    print("Computador: {}".format(placar_maquina))
    print("")
    print("")

    print("Escolha seu lance:")
    print(" 0 - Papel | 1 - Pedra | 2 - Tesoura")
    escolha = int(input())

    voce = lance[escolha]
    computador = lance[random.randrange(3)]

    print("============================")
    print("Sua jogada: {}".format(voce))
    print("Jogada do computador: {}".format(computador))
    print(jokepo(voce,computador))
    print("============================")

    if   jokepo(voce,computador) == "Você ganhou!":
        placar_humano = placar_humano + 1
    elif jokepo(voce,computador) == "Computador ganhou!": 
        placar_maquina = placar_maquina + 1
        
    print("Deseja jogar novamente? 0 - SIM | 1 NÃO")
    jogo = int(input())

    if jogo == 1:
        os.system("cls")
        break
    else:
        os.system("cls")

    
    