# Condições IF,, ELIF e ELSE - Aula 4
'''
if False:
    print('Verdadeiro')
elif True:
    print('Agora é verdadeiro')
else:
    print('Não é verdadeiro.')


# Operadores Relacionais 

num_1 = 2 # int
num_2 = 2 # int

expressao = (num_1 == num_2)
print(expressao)

num_3 = 3 # int
num_4 = 2 # int
expressao = (num_3 > num_4)
print(expressao)

num_5 = 2 # int
num_6 = 5 # int
expressao = (num_3 >= num_4)
print(expressao)
'''

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

#Limite para pegar empréstimo
idade_limite = 18

if idade >= idade_limite:
    print(f'{nome} pode pegar o emprestimo.')
else:
    print(f'{nome} NÃO pode pegar o emprestimo.')
 
# outro exemplo:
    
nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

#Limite para pegar empréstimo
idade_menor = 20 # muito jovem
idade_maior = 30 # passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o emprestimo.')
else:
    print(f'{nome} NÃO pode pegar o emprestimo.')
    
# Operadores Lógicos
# and, or, not
# in e not in

# Um exemplo de quando usar not, quando um valor esta vazio.
a = 0
if not a:
    print('Por favor, preecha o valor de A.')

# in pode ser usando por exemplo para saber se tem uma letra no seu nome
nome = 'Djalma Santos'
if 'n' in nome:
    print("Existe")
else:
    print('Não existe')
 
# in not é o contrário.    
nome = 'Djalma Santos'
if 'asdf '  not in nome:
    print("Executei.")
else:
    print('Existe o texto.')


usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'luiz'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você esta logado no sistema')
else:
    print('Usuário ou senha inválida')
