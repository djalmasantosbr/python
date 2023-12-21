# Este é o(a) #nome #sobrenome. Ele/Ela nasceu em #ano_nascimento e tem #idade anos. #nome #sobrenome tem #altura de altura e pesa #peso kilos.

name ='Djalma' 
sobrenome ='Lima'
idade = 46
altura = 1.68
peso = 105
ano_vigente = 2023
ano_nascimento = ano_vigente - idade

print('Este é o(a) {0} {1}. Ele\Ela nasceu em {2} e tem {3} anos. {0} {1} tem {4} e pesa {5} kilos.'.format(name, sobrenome, ano_nascimento,idade,altura,peso))
print(f'Este é o(a) {name} {sobrenome}. Ele\Ela nasceu em {ano_nascimento} e tem {idade} anos. {name} {sobrenome} tem {altura} e pesa {peso} kilos.')
