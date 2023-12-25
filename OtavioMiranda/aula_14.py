'''
Desenpacotamento de listas 
'''
lista = ['Luiz', 'João', 'Maria']

n1, n2, n3 = lista

print(n2)
print(n1)
print(n3)

# Fazendo desenpacotamento parcial

lista = ['Luiz','João','Maria',1,2,3,4,5]

n1, n2, *outra_lista = lista

print(n1)
print(n2)
print(outra_lista)

# motrando o último da lista
n1, n2, *outra_lista, ultimo_da_lista = lista
print(ultimo_da_lista)

# Pegando os três últimos valores da lista
*outra_lista, n1, n2, n3 = lista
print(n1)
print(n2)
print(n3)

# quando você não for usar o restanta lista usa-se *_
lista = ['Luiz','João','Maria',1,2,3,4,5]
n1, n2, *_ = lista
print(n1, n2)