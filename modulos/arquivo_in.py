# programa para organizar arquivos em pastas

import os
cwd = os.getcwd()
# Criando uma lista com os arquivos da pasta:
arquivo =[]
arquivo = os.listdir(cwd)
novo_arquivo = []

for arq in arquivo:
    if os.path.isfile(arquivo) and '.py' not in arq:
        novo_arquivo.append(arq)
        print(novo_arquivo)

novo_arquivo

# Criando um lista com as extenções dos arquivos da pasta:
ext = []
for valor in arquivo:
    ext.append(valor[-3:])

# Limpando extenções repetidas convertendo a lista em um conjunto
a_ext = set(ext)

# Convertendo novamente em lista novamente sem as extenções repetidas
b_ext = []
for valor in a_ext:
    b_ext.append(valor)

#criando as pastas
for extensao in b_ext:
    os.mkdir(extensao)

# Mostrando os arquivos que pertence a extensão:
for a in arquivo:
    for b in b_ext:
        if a[-3:] == b:
            print("Arquivo: {} tem a extenção: .{}".format(a,b))


    
            





