import random
import os

placar_humano = 0
placar_maquina = 0   

lance = ['Papel','Pedra', 'Tesoura']

# Essa função devolve o resultado da jogada e uma variavel para fazer a soma do placar
def jokepo(voce,computador):
    if (voce == 'Papel' and computador == 'Papel') or (voce == 'Pedra' and computador == 'Pedra') or (voce == 'Tesoura' and computador == 'Tesoura')  :
        resultado = "Empatou..."
        placar = 0
    elif voce == 'Papel' and computador == 'Pedra':
        resultado = "Você ganhou"   
        placar = 1 
    elif voce == 'Pedra' and computador == 'Tesoura':
        resultado = "Você ganhou"  
        placar = 1
    elif voce == 'Tesoura' and computador == 'Papel':
        resultado = "Você ganhou"    
        placar = 1 
    else:
        resultado = "Computador ganhou"  
        placar = 2
    return (resultado, placar)

    
while True:
    
    print("============================================")
    print("Bem vindo ao jogo de Papel, Pedra ou Tesoura")
    print("============================================")
    print("")
    print("PLACAR:")
    print("Você: {}".format(int(placar_humano)))
    print("Computador: {}".format(int(placar_maquina)))
    print("")
    print("")

    print("Escolha seu lance:")
    print(" 0 - Papel | 1 - Pedra | 2 - Tesoura")
    try:
        
        escolha = int(input())

        voce = lance[escolha]
        #Varial que guarda a jogada do computador
        computador = lance[random.randrange(3)]

        print("============================")
        print("Sua jogada: {}".format(voce))
        print("Jogada do computador: {}".format(computador))
        
        # Chamando a função para mostrar o resultado da jogada
        print(jokepo(voce,computador)[0])
        print("============================")
        
        # If para fazer a soma do placar
        if jokepo(voce,computador)[1] == 1:
            placar_humano = placar_humano + 1
        elif jokepo(voce,computador)[1] == 2: 
            placar_maquina = placar_maquina + 1
    except Exception as e:
        print("Erro: {}".format(e))
        
    print("")    
    print("Deseja jogar novamente? 0 - SIM | 1 NÃO")
    try:
        jogo = int(input())

        if jogo != 0:
            os.system("cls")
            break
        else:
            os.system("cls")
    except Exception as e:
        
        print("Erro: {}".format(e))
        print("")    
        print("Deseja jogar novamente? 0 - SIM | 1 NÃO")
        jogo = int(input())

        if jogo != 0:
            os.system("cls")
            break
        else:
            os.system("cls")

    
    