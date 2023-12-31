import os
import random

os.system('cls')
'''
Projeto Jogo da Velha: Montar uma matriz:
A0 - A1 - A2
B0 - B1 - B2
C0 - C1 - C2

Horizontal:
A0 - A1 - A2
B0 - B1 - B2
C0 - C1 - C2
Vertical:
A0 - B0 - C0
A1 - B1 - C1
A2 - B2 - C2
Inclinado:
A0 - B1 - C2
C0 - B1 - A2
'''
# Dicionário
diA = { "a": ['A0', 'A1', 'A2'], "b": ['B0','B1','B2'], "c": ['C0', 'C1', 'C2']}
randomico_computador = [1,2,3,4,5,6,7,8,9]

def escolhe_posicao():
    
    # for para saber quantos valores eu tenho na lista
    soma_valores = 0
    for valores in diA.values():
        soma_valores += len(valores)
    
    # Cria uma lista em um unico paragrafo
    enumera_posicao = 1 # Inicia a posição a ser escolhida
    printa = '' # Onde vai colocar em linha horizantal as posição de escolha
    
    for posicao in diA.values(): # mostra os valores do dicionário
        for valor in posicao:
          if enumera_posicao <= soma_valores:
              printa += f' [{enumera_posicao}] - {valor} | '
              enumera_posicao += 1
    print(printa)           

# Atualiza posição em desenvolvimento
def atualiza_posicao(voce, computador, voceletra):
    escvoce= voce
    esccomptador = computador
    sualetra = voceletra
    
    # coletando a informação do jogador
    if sualetra == 'x' or sualetra == 'X':
        computadorletra = "O"
        sualetra = "X"
    else:
        computadorletra = "X"    
        sualetra = "O"   
    # A0
    if escvoce == 1:
        a[0] = sualetra
        diA['a'][0] = sualetra
    elif esccomptador == 1:
        a[0] = computadorletra
        diA['a'][0] = computadorletra
    # A1
    if escvoce == 2:
        a[1] = sualetra
        diA['a'][1] = sualetra
    elif esccomptador == 2:
        a[1] = computadorletra
        diA['a'][1] = computadorletra 
    # A2
    if escvoce == 3:
        a[2] = sualetra
        diA['a'][2] = sualetra
    elif esccomptador == 3:
        a[2] = computadorletra
        diA['a'][2] = computadorletra
    # B0
    if escvoce == 4:
        b[0] = sualetra
        diA['b'][0] = sualetra
    elif esccomptador == 4:
        b[0] = computadorletra
        diA['b'][0] = computadorletra
    # B1
    if escvoce == 5:
        b[1] = sualetra
        diA['b'][1] = sualetra
    elif esccomptador == 5:
        b[1] = computadorletra
        diA['b'][1] = computadorletra
    # B2
    if escvoce == 6:
        b[2] = sualetra
        diA['b'][2] = sualetra
    elif esccomptador == 6:
        b[2] = computadorletra
        diA['b'][2] = computadorletra
    # C0
    if escvoce == 7:
        c[0] = sualetra
        diA['c'][0] = sualetra
    elif esccomptador == 7:
        c[0] = computadorletra
        diA['c'][0] = computadorletra
    # C1
    if escvoce == 8:
        c[1] = sualetra
        diA['c'][1] = sualetra
    elif esccomptador == 8:
        c[1] = computadorletra
        diA['c'][1] = computadorletra
    # C2
    if escvoce == 9:
        c[2] = sualetra
        diA['c'][2] = sualetra
    elif esccomptador == 9:
        c[2] = computadorletra
        diA['c'][2] = computadorletra
        
# Apresentação do jogo da velha
def logo():
    print('=======================================')    
    print('      ***** JOGO DA VELHA *****')
    print('=======================================')  
    print('')

# função if  para tratar a letra que o jogador escolheu
def escolha(resp):
    if resp == 'x' or resp == 'X':
        computador = 'O'
        voce = 'X'
        resposta = print(f'Você letra: {voce} | Computador letra: {computador}')
    
    elif resp == 'o' or resp == 'O':
        computador = 'X'
        voce = 'O'
        resposta = print(f'Você letra: {voce} | Computador letra {computador}')
    return resposta

def jogacomputador(n):
    po_voce = n
    randomico_computador.remove(n)
    if len(randomico_computador) > 1:
        po_comp = random.choice(randomico_computador)
        randomico_computador.remove(po_comp)
    else:
        po_comp = randomico_computador
    return po_comp

def valida(let_, a, b, c):
    
    if let_ == 'x' or let_ == 'X':
        cop= "O"
        let_= "X"
    else:
        cop= "X"    
        let_ = "O"  
        
    resposta = ''
    if ((a[0] == a[1] == a[2] == let_) or (b[0] == b[1] == b[2] == let_) or (c[0] == c[1] == c[2] == let_) or (a[0] == b[0] == c[0] == let_) or 
        (a[1] == b[1] == c[1] == let_) or (a[2] == b[2] == c[2] == let_) or (a[0] == b[1] == c[2] == let_) or (c[0] == b[1] == a[2] == let_)):
        
        resposta = 'VOCÊ ganhou!!!'
        
        
    elif (a[0] == a[1] == a[2] == cop or (b[0] == b[1] == b[2] == cop) or (c[0] == c[1] == c[2] == cop) or (a[0] == b[0] == c[0] == cop) or 
        (a[1] == b[1] == c[1] == cop) or (a[2] == b[2] == c[2] == cop) or (a[0] == b[1] == c[2] == cop) or (c[0] == b[1] == a[2] == cop)):
        
        resposta = 'COMPUTADOR ganhou!!!'
    
    return resposta
 
 # Painel       
def painel():
    print('')
    print('           0 | 1 | 2')
    print('          -----------')
    print(f'        A  {a[0]} | {a[1]} | {a[2]}')
    print('          -----------')
    print(f'        B  {b[0]} | {b[1]} | {b[2]}')
    print('          -----------')
    print(f'        C  {c[0]} | {c[1]} | {c[2]}')
    print('          -----------')
    print('')
    

def resultado():
    result = valid
    if len(result) > 0:
        logo()
        painel()
        print()
        return
 
''' 
def xouy():
     
     while True:
        letra = input('Escolha com qual letra você quer jogar: "X" ou "O":\n')
        letra = letra.upper() # Converte para maiuscula
    
        if letra == 'X' or letra == 'O':
            break
        return letra
'''
        
# input para o jogador escolher a letra    
logo()
print()

while True:
    letra = input('Escolha com qual letra você quer jogar: "X" ou "O":\n')
    letra = letra.upper() # Converte para maiuscula
    
    if letra == 'X' or letra == 'O':
        break         
    
#letra_= xouy()        
        
os.system('cls')

a = []
b = []
c = []

cont = 0
while cont <= 2:
    a.append(' ')
    b.append(' ')
    c.append(' ')
    cont += 1

while True:
    
    # Função
    logo()
    # Função
    escolha(letra)
    # Painel
    painel()
    print(f'Escolha a posição que você quer jogar a letra "{letra.upper()}", digitando o número da posição:')
    print('') 
    # Função 
    
    # Variáveis
    while True:
        escolhe_posicao()
        po_escolhida_voce = input()
        
        if not  po_escolhida_voce.isnumeric():
            os.system('cls')
            logo()
            escolha(letra)
            painel()
            
        else:
            break
                 
    # Função com variavel
    joga_computador = jogacomputador(int(po_escolhida_voce))
    # Função
    atualiza_posicao(int(po_escolhida_voce), joga_computador, letra)
    valid = valida(letra, a, b, c)
    if len(valid) > 0:
        os.system('cls')
        logo()
        escolha(letra)
        painel()
        print('')
        print(valid)
        print('')
        break
    elif len(randomico_computador) == 0:
        print('')
        print('Houve um EMPATE!!! \n')
        while True:
            opcao = input('Quer jogar novamente: 1 - "SIM" 2 = "NÃO"\n')
            if not opcao.isnumeric():
                print("opção invalida...")
            elif opcao == 1:
                pass
            elif opcao == 2:
                break
            else:
                print('Opção invalida...')
        
        
        
    os.system('cls')
    print("")
    # os.system('cls')
    
 


