'''
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
'''
texto = 'Python'

for letra in texto:
    print(letra)

# Enumerate - Enumera o indice
for n, letra in enumerate(texto):
    print(n, letra)

# Função range(start=0, stop, step=1)

for n in range(10):
    print(n)

# range começando de 10 até 20
for n in range(10,21):
    print(n)

# range começando de 20 até 10 usar step -1
for n in range(20, 9, -1):
    print(n)

# range começando de 0 até 10 pulando de 2 em 2
for n in range(0, 11, 2):
    print(n)

# Exemplos de encontrar multiplos de 8 até 100:
for n in range(0,100,8):
    print(n)

print('#############')
print('')

for n in range(100):
    if n % 8 == 0:
        print(n)

texto = 'Python'
nova_string = ''
for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)

# continue - pula para o proximo laço
# break - Termina o laço



