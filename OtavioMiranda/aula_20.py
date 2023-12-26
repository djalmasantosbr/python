
import copy
d1 = {
    'str' : 'valor',
    123 : "Outro valor",
    (1,2,3,4) : 'Tupla',
}


print(d1)

# Dicionário - For

clientes = {
    'Cliente1' : {
        'nome': "Luiz",
        'sobrenome': 'Otávio',
    },
     'Cliente2' : {
        'nome': "JOão",
        'sobrenome': 'Moreira',
    },
      'Cliente3' : {
        'nome': "Maria",
        'sobrenome': 'Otávio',
    },
    
}

for clintes_k, clientes_v in clientes.items():
    print(f'Exibindo {clintes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')


# criando copia do dicionário

d1 = {1: 'a', 2: 'b', 3: 'c'}
v = d1

v[1] = 'Luiz'
# Dessa forma não cria uma nova variavel.
print(d1) # {1: 'Luiz', 2: 'b', 3: 'c'}
print(v) # {1: 'Luiz', 2: 'b', 3: 'c'}

# impot copy - copy.deepcopy()  - para copiar um dicionário
d1 = {1: 'a', 2: 'b', 3: 'c,', 'd': ['Luiz', 'Otávio']}
v = copy.deepcopy(d1)

v[1] = 'Luiz'
v['d'][0] = 'Joazinho'

print(d1)
print(v)


