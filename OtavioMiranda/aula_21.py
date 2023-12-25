'''
Projeto de perguntas e respostas com dicionário em Python
'''
# Usndo dicionário em python

perguntas = {
    'Pergunta 1': {
        'Pergunta': 'Quanto é 2 + 2?',
        'respostas': {'a': '1','b': '4','C': '5',},
        'resposta_certa': 'b',
    },
    
    'Pergunta 2': {
        'Pergunta': 'Quanto é 3 * 2?',
        'respostas': {'a': '4','b': '10','C': '6',},
        'resposta_certa': 'c',
    },
    'Pergunta 3': {
        'Pergunta': 'Quanto é 4 / 4?',
        'respostas': {'a': '1','b': '4','C': '5',},
        'resposta_certa': 'a',
    },
}

respostas_certas = 0
for pk, pv in perguntas.items():
    print('')
    print(f'{pk}: {pv["Pergunta"]}')
    
    print('Respostas:')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta:')
    
    if resposta_usuario == pv['resposta_certa']:
        print('Resposta correta: {}'.format(pv['resposta_certa']))
        respostas_certas += 1
    else:
        print('Voce errou.....')
    print()
    
qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi {porcentagem_acerto:.2f}%.')