# (adcional), update (atualiza), clear, dicard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)

s1 = {1,2,3,4,5}

print(s1)

for v in s1:
    print(v)

s2 = set() # para criar um conjunto vazio

# .add() - adiciona 

s2.add(1)
s2.add(2)
s2.add((1,2,3,'Luiz'))

print(s2)

# removendo uma posição

s2.discard(2)
print(s2)

# update
s3 = set()
s3.update('Python') # não obedece ordem dos elementos
print(s3)

# elimiando elementos duplicado de uma lista

l1 = [1,1,1,2,2,23,4,4,5,6,7,8,9, 10, 'Luiz', "Luiz"]
print(l1)
l1 = set(l1) # transformou a lista em um conjunto
print(l1)
l1 = list(set(l1))
print(type(l1))

# Funções do set

s4 = {1,2,3,4,5,7}
s5 = {1,2,3,4,5,6}
s6 = s4 | s5 # union
print(s6) # union

s7 = s4 & s5 # intersecção
print(s7)

s8 = s4 - s5 # Elementos apenas no set da esquerda
print(s8)
s9 = s5 - s4 # Elementos apenas no set da esquerda
print(s9)

# symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)

s10 =  s4 ^s5 #
print(s10) 

