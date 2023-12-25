'''
Operador ternário em Python
'''
# Exemplo comum

logged_user = False # pode ser True: mostrará a resposta no else

if logged_user:
    msg = 'usuário logado'
else:
    msg = 'Usuário precisa logar'

print(msg)

# Operador ternário

logged_user = False
msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'
print(msg)

logged_user = True
msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'
print(msg)

# mais um exemplo a pessoa é maior de 18 anos

idade = 17

if idade >= 18:
    print("pode acessar o sistema.")
else:
    print('Não pode acessaro sistema.')
    
maior_idade = 'Pode acessar o sistema' if idade >=18 else 'Não pode acessar o sistema'
print(maior_idade)

# Mais um exemplo com imput

idade = input('Qual a sua idade? ')   

if not idade.isnumeric():
    print('Você precisa digitar apenas números')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'Pode acessar' if e_de_maior else 'Não Pode acessar.'
    
    print(msg)
    
    
