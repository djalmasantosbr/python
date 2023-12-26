# Geradores, interadores, interaveis

lista = [0,1,2,3,4,5] # interavel
#lista = 122345 # Não interavel
#lista = 'String' # interavel
print(hasattr(lista, '__iter__'))

for v in lista:
    print(v)



