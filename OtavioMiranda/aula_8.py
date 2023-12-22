'''
while / else - Aula 8
contadores
acumuladores
'''

contador = 90
while contador <=100:
    print(contador)
    contador += 1

# acumulador e else
contador = 1
acumulador = 1

while contador <=10:
    print(contador, acumulador)
    
    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else')
    
# acumulador e else e comando break
contador = 1
acumulador = 1

while contador <=10:
    print(contador, acumulador)
    
    if contador > 5:
        break
    
    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else')

print('Isso será executado.')