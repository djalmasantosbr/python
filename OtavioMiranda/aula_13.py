'''
Split - Dividir uma string #str
Join - Juntar uma lista #str
Enumerate - Enumerar elementos da lista #interáveis
'''
string = "O Brasil é o país do futebol, o Brasil é penta"

# Função split

lista1 = string.split(' ')
lista2 = string.split(',')

print(lista1)
print(lista2)

for valor in lista1:
    print(valor)

for valor in lista2:
    print(valor)
    
for valor in lista1:
    print(f'A palavra {valor} apareceu {lista1.count(valor)}x na frase')

palavra = ''
contagem = 0
for valor in lista1:
    qtd_vezes = lista1.count(valor)
    
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')

for valor in lista2:
    print(valor)

# para resolver o problema após a divisão a frazer ter um espaço e
# a primeira letra ficar em ninusculo usa-se:
# strip() - para eliminar os espaços vazios
# capitalize() - para deixar a primeira letra maiúscula.

for valor in lista2:
    print(valor.strip().capitalize())
    
# Join - Juntar uma lista #str

lista3 = 'O Brasil é penta'
lista4 = lista3.split(' ')
lista5 = ','.join(lista4)

print(lista5)
print('')
print(lista4)

# Enumerate - Enumerar elementos da lista #interáveis
lista6 = ['Luiz', 'João', 'Maria']
for indice, nome in enumerate(lista6):
    print(indice, nome)
    