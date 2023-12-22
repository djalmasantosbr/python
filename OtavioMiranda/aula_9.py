'''
Interagindo strings com while em python
'''

minha_string = 'o rato roeu a roupa do rei de roma'
tamanho_string = len(minha_string)
c = 0

while c < tamanho_string:
    print(c, minha_string[c])
    c += 1
print('tamanho_string: {}'.format(tamanho_string))

# Exemplo de mudar todos os 'r' da frase para maiúsculo.

minha_string = 'o rato roeu a roupa do rei de roma'
tamanho_string = len(minha_string)
c = 0
nova_string = ''
while c < tamanho_string:
    
    if minha_string[c] == 'r':
        nova_string = nova_string + minha_string[c].upper()
    else:
       nova_string =  nova_string + minha_string[c]
    c += 1
print(nova_string)

# .count() mostra quantas vezez aparece a letra que você escolheu
print(minha_string.count('r'))

# qual letra aparece mais dentro de uma frase
# .strip() ele elemina os espaços da frase

minha_string = 'o rato roeu a roupa do rei de roma.'
c = 0
contagem_atual = 0
letra = ''
while c < tamanho_string:
    qtd_vezes_letra = minha_string.count(minha_string[c])
    
    if contagem_atual < qtd_vezes_letra and minha_string[c].strip():
        letra = minha_string[c]
        contagem_atual = qtd_vezes_letra
    #print(minha_string[c], conta )
    c += 1
print(f'A letra "{letra}", apareceu {contagem_atual} vezez.')

# Criando um laço onde o programa faz a pergunta: 
while True:
    minha_string = input('Digite uma frase:')
    tamanho_string = len(minha_string)
    c = 0
    contagem_atual = 0
    letra = ''
    while c < tamanho_string:
        qtd_vezes_letra = minha_string.count(minha_string[c])
        
        if contagem_atual < qtd_vezes_letra and minha_string[c].strip():
            letra = minha_string[c]
            contagem_atual = qtd_vezes_letra
        #print(minha_string[c], conta )
        c += 1
    print(f'A frase: "{minha_string}"')
    print(f'A letra "{letra}", apareceu {contagem_atual} vezez.')
    print('\n')
    
    # Recapitulando
    c = 0
    string = 'valor'
    while c < len(string):
        print(string[c])
        c += 1
        