
# isso é  um comentário
pass # Isso também é um comentário
print('Linha 1')
print('Linha 2')
#print('Linha 3')
print('Linha 4')
print('Linha 5')
print('Linha 6')

# Exibe: Aspas duplas e aspas simples.
print("Aspas duplas", 'Aspas simples')

#Aspas dentro de aspas
print("aspas \"isso esta dentro de aspas\" duplas")

# Exemplos abaixo:
print("Aqui eu mostro 'aspas simples' dentro de aspas duplas.")
print('Aqui eu mostro "aspas duplas" dentro de aspas simples.')
print("aqui eu mostro \"aspas duplas\" dentro de aspas duplas.")
print('Aqui eu mostro \'aspas simples\' dentro de aspas simples.')

# Exemplos de numeros sem aspas

print('A soma de 5+5 é:', 5+5)
print('Número tratado com texto:', '5' + '5')
print(-5.55*2) # multiplicação | Exipe: -11.1
print('-.55'*2) #Repetição | Exibe: -5.55-5.55

# O python difencia letras maiúscas de letras minúsculas em suas intruções
# Com isso Print() e print() são duas coisas diferentes.

# Para hierarquia de códigos o python usa espaços chamaos isso de identação.

# Operadores aritiméticos
# As operações de mesma prioridade são realizados da esquerda paa direita.
# Os parenteses alteram a propriedade

print('Soma 2 com 2:', 2 + 2) # 4
print('Concatena 2 com 2:', '2' + '2') # 22
print('Multiplica 2 com 2:', 2*2) # 4
print('Repete "A" 5 vezes:', 'A'*5) # AAAAA
print('Divide 10 com 3:', 10/3) # 3.3333333333333335
print('Divide 10 com 3 (valor inteiro):', 10//3) # 3
print('Resto da divisão entre 10 e 3:', 10%3) # 1
print('2 elevado a 3:', 2**3) # 8
print('Alterando a prioridade:', (5+2)*10) # (5+2) = 7, 7*10 = 70

# Variáveis é para armazernar valores na memória

nome = 'Djalma Santos' # string
idade = 46 # int
altura = 1.80 # float
peso = 100 # inteiro
data_atual = '21/12/2023' #string


# Fórmula IMX = peso divido pelo  quadrado da altura
indice_massa_corporal = peso / (altura ** 2)
indice_massa_corporal = '{:.2f}'.format(indice_massa_corporal)

print('A variavel nome recebeu:', nome)
print('A variavel idade recebeu:', idade)
print('A variavel data recebeu:', data_atual)
print(nome, 'tem', idade, 'anos e seu IMC é', indice_massa_corporal)
print('{} tem {} e seu IMC  é {}.'.format(nome,idade,indice_massa_corporal))
print('{n} tem {i} anos e seu IMC é {c}'.format(n=nome, i=idade, c=indice_massa_corporal)) # posso repetir a variavel dentro {}
print('{0} tem {1} anos e seu IMC é {2}'.format(nome, idade, indice_massa_corporal)) # posso repetir o indice dentro {}
# Outro exemplo ainda mais interessante:
print(f'{nome} tem {idade} anos e seu IMC é {indice_massa_corporal}')

# Tipos de dados

inteiro = 5 # int
real = 5.5 # float
booleano = True # bool
texto = '5.5' # str

# Cast (convertendo string em float)
texto_float = float(texto)
print((texto_float + real)) # 11.0

# int + float
print(inteiro + real) # 10.5
# int / float
print(inteiro / real) # 0.9090909090909091

# Cast (convertendo string em float)
texto_float = float(texto)
print(texto_float + real) # 11.0

# int + float
print(inteiro + real) # 10.5

# Cast (convertendo float em inteiro)
float_inteiro = int(real)

variavel = 10>2
print(variavel)

variavel = 10<2
print(variavel)

# Passando uma variavel inteiro para string
print('O tipo de variável inteiro é:', type(inteiro)) # int
inteiro = str(inteiro) # str
print('O tipo da variável agora é', type(inteiro))


