'''
Funções - def em Python (parte 1)
'''

# Exemplo de uma função sem retornar parametro
def funcao():
    print('Olá mundo!')

funcao()

# Retornando parametro
def saudacao(nome):
    resposta = print(f'Bom dia {nome}!')

saudacao('Djalma')


# return

def  printar(var):
    print(var)
    
variavel = printar('Valor que eu quero')
print(variavel) #Valor que eu quero None -> valor vazio

# Resolvendo o valor vazio None

def printar(var):
    print(var)
    
variavel = printar('Valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum valor.')

# Solução

def printar(var):
    return var
    
variavel = printar('sou feliz')

if variavel:
    print(variavel)
else:
    print('Nenhum valor.')
    
# def divisão

def divisao(n1, n2):
    if n2 > 0:
        return n1 /n2

divide = divisao(8,1)

if divide:
    print(divide)
else:
    print("Conta invalida")
    
# Mais um exemplo
def divisao(n1, n2):
    if n2 == 0:
        return 
    return n1 / n2

divide = divisao(8,0)

if divide:
    print(divide)
else:
    print("Conta invalida")
    
# * args **kwargs

# https://www.youtube.com/watch?v=_Rkr8LsH9BA&list=PLbIBj8vQhvm0ayQsrhEf-7-8JAj-MwmPr&index=20


def func(*args):
    print (args)
    print(args[0])
    print(args[-1])
    print(len(args))
    
func(1,2,3,4,5)
       
lista =  [1,2,3,4,5]
print(*lista, sep='-')

# cast
def func(*args):

    args = list(args)
    args[0] = 20
    print(args)
    
func(1,2,3,4,5)

#for
def func(*args):
    for v in args:
        print(v)
    
func(1,2,3,4,5)


# Tupla
def func(*args):
    print(args)

lista = [1, 2, 3, 4, 5]
func(lista, '6')

#Desenpacotar *lista
def func(*args):
    print(args)

lista = [1, 2, 3, 4, 5]
func(*lista)

# desenpacotando duas listas

def func(*args):
    print(args)

lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]

func(*lista, *lista2)

# *args **kwargs

def func(*args, **kwargs):

    print(args)
    print(kwargs)
    print(kwargs['nome'], kwargs['sobrenome'])

lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Luiz', sobrenome='Miranda')

# outro exemplo com get

def func(*args, **kwargs):
    print(args)
    
    idade = kwargs.get('idade')
    
    if idade is not None:
        print(idade)
     

lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Luiz', sobrenome='Miranda', idade = 30)

# sem get

def func(*args, **kwargs):
    print(args)
    
    idade = kwargs['idade']
    print(idade)
     

lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Luiz', sobrenome='Miranda', idade = 30)

# Escopo de variáveis funções python

