'''
While em Python - Aula 7
utilizado para realizar ações enquanto um condição for verdadeira
Requisitos: entender condições e operadores

while True:
    nome = input('Qual o seu nome? ')
    print(f'Olá {nome}!')
 '''   
x = 0
while x < 5:
    print(x)
    x += 1
print('Acabou')

# continue
x = 0
while x < 10:
    if x == 3:
        x += 1
        continue
    
    print(x)
    x += 1
print('Acabou')

# break
x = 0
while x < 10:
    if x == 3:
        x += 1
        break
    
    print(x)
    x += 1
print('Acabou')

x = 0 # coluna
while x < 10:
    y = 0 # linha
    while y < 5:
        print(f'x vale {x} e Y vale {y}')
        y += 1
    x += 1
print('Acabou')

x = 0 # coluna
while x < 10:
    y = 0 # linha
    while y < 5:
        print(f'({x},{y})')
        y += 1
    x += 1
print('Acabou')


