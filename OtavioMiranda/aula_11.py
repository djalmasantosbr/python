'''
https://www.youtube.com/watch?v=CSTb7pLsLZE&list=PLbIBj8vQhvm0ayQsrhEf-7-8JAj-MwmPr&index=14&t=12s
Lista em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
'''
lista = ['A', 'B', 'C', 'D', 'E', 10.5]

# Listando o indice 5º da lista
print(lista[5])

# Fazendo fatiamento da lista. Ele lista os primeiros 3 indices.
print(lista[0:3])

#Exemplos de fatiamento
print(lista[:3])
print(lista[2:])
print(lista[-1])
print(lista[0])
print(lista[::2])
print(lista[::-1])

# Exemplos append, insert, pop, del, clear, extend, +

l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2


print(l1)
print(l2)
print(l3)

# Extend
l1.extend(l2)
print(l1)

l1.extend('a')
print(l1)
print(l1[3])

# insert - Inserindo o valor no indice que eu queira

l2.insert(0, 'banana')
print(l2)
print(l2[0])

# pop - revomendo o último  valor 
l5 =[7,8,9]
print(l5)
l5.insert(0,'banana')
print(l5)
l5.pop()
print(l5)

# pop - removendo um valor colocando um indice

l6 = [1,2,3,4,5,7,8,9]
print(l6)
l6.insert(0,'banana')
print(l6)
del(l6[0])
print(l6)

# max - maximo da lista | min - minimo da lista

print(max(l6))
print(min(l6))

# Criando uma lista com o comando range

l10  = list(range(1,10))
print(l10)

# Exemplo para discobriu o tipo de elemento que consta em uma lista

l11 = ['String', True, 10, -20.5]

for elem in l11:
    print(f'O tipo de elemento {elem} é {type(elem)}.')
