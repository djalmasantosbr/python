import os

sn = 0
while sn == 0:
    print('============ C A L C U L A D O R A ==========')
    print('')
    print('0 : Soma')
    print('1 : Subtração')
    print('2 : Multiplicação')
    print('3 : Divisão')
    print('4 : Exponenciação')
    print('')
    print('Escolha a operação que deseja realizar:')
    op = int(input())

    if op == 0:
        print('')
        print('')
        print('>>> + escolhida.')
        print('')
        print('')
        print('Digite o primeiro valor:')
        som = [float(input())]
        print('digite o segundo valor:')
        som.append(float(input()))

        soma = som[0] + som[1]

        print('')
        print('')
        print('')
        print('{} + {} = {}'.format(som[0], som[1], soma))

    elif op == 1:
        print('')
        print('')
        print('>>> - escolhida.')
        print('')
        print('')
        print('Digite o primeiro valor:')
        sub = [float(input())]
        print('digite o segundo valor:')
        sub.append(float(input()))

        subtr = sub[0] - sub[1]

        print('')
        print('')
        print('')
        print('{} - {} = {}'.format(sub[0], sub[1], subtr))

    elif op == 2:
        print('')
        print('')
        print('>>> * escolhida.')
        print('')
        print('')
        print('Digite o primeiro valor:')
        mult = [float(input())]
        print('digite o segundo valor:')
        mult.append(float(input()))

        multiplica = mult[0] * mult[1]

        print('')
        print('')
        print('')
        print('{} * {} = {}'.format(mult[0], mult[1], multiplica))

    elif op == 3:
        print('')
        print('')
        print('>>> / escolhida.')
        print('')
        print('')
        print('Digite o primeiro valor:')
        div = [float(input())]
        print('digite o segundo valor:')
        div.append(float(input()))

        divisa = div[0] / div[1]

        print('')
        print('')
        print('')
        print('{} / {} = {}'.format(div[0], div[1], divisa))

    else:
        print('')
        print('')
        print('>>> ^^ escolhida.')
        print('')
        print('')
        print('Digite o primeiro valor:')
        exp = [float(input())]
        print('digite o segundo valor:')
        exp.append(float(input()))

        expo = exp[0] - exp[1]

        print('')
        print('')
        print('')
        print('{} ^^ {} = {}'.format(exp[0], exp[1], expo))

    print('')
    print('')   
    print('Deseja fazer outra operação? 0 - SIM, 1 - NÃO')
    sn = int(input())
    os.system('cls')

print('')
print('Desconectando...')


      




