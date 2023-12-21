'''
Formatando valores com modificadores - Aula 5

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO -s, d ou f)

> - Esquerda
< - Direita
^ - Centro
'''
num_1 = 10
nun_2 = 3
divisao = num_1 / nun_2
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

# :s - Texto (strings)
nome = 'Luiz Otávio'
print(f'{nome:s}')

# :(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO -s, d ou f)
num_1 = 1
print(f'{num_1:0>10}') # 0000000001

num_2 = 1150
print(f'{num_2:0>10}') # 0000001150

num_1 = 1
print(f'{num_1:0<10}') # 1000000000

num_2 = 1150
print(f'{num_2:0<10}') # 1150000000

num_2 = 1150
print(f'{num_2:0^10}') # 0001150000

# :.(NÚMERO)f - Quantidade de casas decimais (float)
# Colocando casa decimais em numeros inteiros
num_2 = 1150
print(f'{num_2:.2f}') # 1150.00

num_2 = 1150
print(f'{num_2:0>10.2f}') # 0001150.00

# Adcionando caracteres em um nome. Deixando o nome da variavel no centro
nome = 'Djalma Santos'
print(len(nome))
print( 50-len(nome))
print(f'{nome:#^50}')

nome_formatado = '{:@>50}'.format(nome)
print(nome_formatado) # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Djalma Santos

nome_formatado = '{:@>13}'.format(nome)
print(nome_formatado) # Djalma Santos - O nome já tem 13 caracteres

nome_formatado = '{n} {n}'.format(n=nome)
print(nome_formatado) # Djalma Santos Djalma Santos

nome_formatado = '{n:0<20}'.format(n=nome)
print(nome_formatado) # Djalma Santos0000000

nome = 'Djalma'
sobrenome = 'Miranda'
nome_formatado = '{0:$^20} {1:#^20}'.format(nome, sobrenome)
print(nome_formatado) # Djalma Miranda


nome = 'Djalma Santos'
print(nome.lower()) # Tudo minusculo
print(nome.upper()) # Tudo maiusculo
print(nome.title()) # Primeiras letras maiusculas


